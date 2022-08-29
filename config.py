from libqtile import bar, layout, widget
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal
import os

mod = 'mod4'
terminal = guess_terminal()
rofi = os.path.expanduser('~/.nix-profile/bin/rofi')
rofi = rofi if os.path.exists(rofi) else 'rofi'

keys = [
    # Switch between windows
    Key([mod], 'h', lazy.layout.left(), desc='Move focus to left'),
    Key([mod], 'l', lazy.layout.right(), desc='Move focus to right'),
    Key([mod], 'j', lazy.layout.down(), desc='Move focus down'),
    Key([mod], 'k', lazy.layout.up(), desc='Move focus up'),
    Key(
        [mod],
        'space',
        lazy.spawn(f'{rofi} -show'),
        desc='Launch rofi',
    ),
    # Move windows between left/right columns or move up/down in current stack.
    # Moving out of range in Columns layout will create new column.
    Key(
        [mod, 'shift'],
        'h',
        lazy.layout.shuffle_left(),
        desc='Move window to the left',
    ),
    Key(
        [mod, 'shift'],
        'l',
        lazy.layout.shuffle_right(),
        desc='Move window to the right',
    ),
    Key(
        [mod, 'shift'],
        'j',
        lazy.layout.shuffle_down(),
        desc='Move window down',
    ),
    Key([mod, 'shift'], 'k', lazy.layout.shuffle_up(), desc='Move window up'),
    # Grow windows. If current window is on the edge of screen and direction
    # will be to screen edge - window would shrink.
    Key(
        [mod, 'control'],
        'h',
        lazy.layout.grow_left(),
        desc='Grow window to the left',
    ),
    Key(
        [mod, 'control'],
        'l',
        lazy.layout.grow_right(),
        desc='Grow window to the right',
    ),
    Key(
        [mod, 'control'], 'j', lazy.layout.grow_down(), desc='Grow window down'
    ),
    Key([mod, 'control'], 'k', lazy.layout.grow_up(), desc='Grow window up'),
    Key([mod], 'n', lazy.layout.normalize(), desc='Reset all window sizes'),
    # Toggle between split and unsplit sides of stack.
    # Split = all windows displayed
    # Unsplit = 1 window displayed, like Max layout, but still with
    # multiple stack panes
    Key(
        [mod, 'shift'],
        'Return',
        lazy.layout.toggle_split(),
        desc='Toggle between split and unsplit sides of stack',
    ),
    Key([mod], 'Return', lazy.spawn(terminal), desc='Launch terminal'),
    # Toggle between different layouts as defined below
    Key([mod], 'Tab', lazy.next_layout(), desc='Toggle between layouts'),
    Key([mod], 'w', lazy.window.kill(), desc='Kill focused window'),
    Key([mod, 'control'], 'r', lazy.reload_config(), desc='Reload the config'),
    Key([mod, 'control'], 'q', lazy.shutdown(), desc='Shutdown Qtile'),
    Key(
        [mod],
        'r',
        lazy.spawncmd(),
        desc='Spawn a command using a prompt widget',
    ),
    # Multimedia keys
    Key(
        [],
        'XF86AudioLowerVolume',
        lazy.spawn('amixer -q -D pulse sset Master 5%-'),
        desc='Low volume',
    ),
    Key(
        [],
        'XF86AudioRaiseVolume',
        lazy.spawn('amixer -q -D pulse sset Master 5%+'),
        desc='Increase volume',
    ),
    Key(
        [],
        'XF86AudioMute',
        lazy.spawn('amixer -D pulse set Master 1+ toggle'),
        desc='Mute',
    ),
    Key(
        [],
        'XF86AudioPlay',
        lazy.spawn('playerctl play-pause'),
        desc='Play/Pause',
    ),
    Key(
        [],
        'XF86AudioNext',
        lazy.spawn('playerctl next'),
        desc='Next',
    ),
    Key(
        [],
        'XF86AudioPrev',
        lazy.spawn('playerctl previous'),
        desc='Previous',
    ),
]

groups = [Group(i) for i in '123456789']

for i in groups:
    keys.extend(
        [
            # mod1 + letter of group = switch to group
            Key(
                [mod],
                i.name,
                lazy.group[i.name].toscreen(),
                desc='Switch to group {}'.format(i.name),
            ),
            # mod1 + shift + letter of group = switch to & move focused window
            # to group
            Key(
                [mod, 'shift'],
                i.name,
                lazy.window.togroup(i.name, switch_group=True),
                desc='Switch to & move focused window to group {}'.format(
                    i.name
                ),
            ),
            # Or, use below if you prefer not to switch to that group.
            # # mod1 + shift + letter of group = move focused window to group
            # Key([mod, "shift"], i.name, lazy.window.togroup(i.name),
            #     desc="move focused window to group {}".format(i.name)),
        ]
    )

catppuccin_mocha = {
    'rosewater': '#f5e0dc',
    'flamingo': '#f2cdcd',
    'pink': '#f5c2e7',
    'mauve': '#cba6f7',
    'red': '#f38ba8',
    'maroon': '#eba0ac',
    'peach': '#fab387',
    'yellow': '#f9e2af',
    'green': '#a6e3a1',
    'teal': '#94e2d5',
    'sky': '#89dceb',
    'sapphire': '#74c7ec',
    'blue': '#89b4fa',
    'lavender': '#b4befe',
    'text': '#cdd6f4',
    'subtext1': '#bac2de',
    'subtext0': '#a6adc8',
    'overlay2': '#9399b2',
    'overlay1': '#7f849c',
    'overlay0': '#6c7086',
    'surface2': '#585b70',
    'surface1': '#45475a',
    'surface0': '#313244',
    'base': '#1e1e2e',
    'mantle': '#181825',
    'crust': '#11111b',
}

layout_config = {
    'border_width': 2,
    'margin': 8,
    'border_focus': catppuccin_mocha['lavender'],
    'border_normal': catppuccin_mocha['overlay0'],
}


layouts = [
    layout.MonadTall(**layout_config),
    layout.Max(**layout_config),
    layout.Floating(**layout_config),
    layout.Tile(**layout_config),
    # Try more layouts by unleashing below layouts.
    # layout.Columns(border_width=4),
    # layout.Stack(num_stacks=2),
    # layout.Bsp(),
    # layout.Matrix(),
    # layout.MonadWide(),
    # layout.RatioTile(),
    # layout.TreeTab(),
    # layout.VerticalTile(),
    # layout.Zoomy(),
]

widget_defaults = dict(
    font='Inter Regular',
    fontsize=12,
    padding=3,
)
extension_defaults = widget_defaults.copy()

screens = [
    Screen(
        top=bar.Bar(
            [
                widget.Sep(
                    linewidth=0,
                    padding=6,
                    foreground=catppuccin_mocha['text'],
                    background=catppuccin_mocha['base'],
                ),
                widget.TextBox(
                    '',
                    fontsize=30,
                    background=catppuccin_mocha['base'],
                    foreground=catppuccin_mocha['text'],
                ),
                widget.TextBox(
                    text='|',
                    background=catppuccin_mocha['base'],
                    foreground=catppuccin_mocha['text'],
                    padding=2,
                    fontsize=14,
                ),
                widget.CurrentLayout(
                    background=catppuccin_mocha['base'],
                    foreground=catppuccin_mocha['text'],
                ),
                widget.TextBox(
                    text='|',
                    background=catppuccin_mocha['base'],
                    foreground=catppuccin_mocha['text'],
                    padding=2,
                    fontsize=14,
                ),
                widget.GroupBox(
                    disable_drag=True,
                    fontsize=14,
                    # margin_y=4,
                    # margin_x=0,
                    # margin=4,
                    # padding_y=5,
                    # padding_x=5,
                    # borderwidth=3,
                    highlight_method='block',
                    inactive=catppuccin_mocha['overlay1'],
                    active=catppuccin_mocha['text'],
                    this_current_screen_border=catppuccin_mocha['surface2'],
                    this_screen_border=catppuccin_mocha['surface2'],
                    other_current_screen_border=catppuccin_mocha['crust'],
                    other_screen_border=catppuccin_mocha['crust'],
                ),
                widget.TextBox(
                    text='|',
                    background=catppuccin_mocha['base'],
                    foreground=catppuccin_mocha['text'],
                    padding=2,
                    fontsize=14,
                ),
                widget.Prompt(),
                widget.WindowName(
                    background=catppuccin_mocha['base'],
                    foreground=catppuccin_mocha['text'],
                ),
                widget.Chord(
                    chords_colors={
                        'launch': ('#ff0000', '#ffffff'),
                    },
                    name_transform=lambda name: name.upper(),
                ),
                widget.TextBox(
                    text='|',
                    background=catppuccin_mocha['base'],
                    foreground=catppuccin_mocha['text'],
                    padding=2,
                    fontsize=14,
                ),
                widget.TextBox(
                    '',
                    background=catppuccin_mocha['base'],
                    foreground=catppuccin_mocha['text'],
                    fontsize=18,
                ),
                widget.Memory(
                    background=catppuccin_mocha['base'],
                    foreground=catppuccin_mocha['text'],
                ),
                widget.TextBox(
                    text='|',
                    background=catppuccin_mocha['base'],
                    foreground=catppuccin_mocha['text'],
                    padding=2,
                    fontsize=14,
                ),
                widget.TextBox(
                    '',
                    background=catppuccin_mocha['base'],
                    foreground=catppuccin_mocha['text'],
                    fontsize=12,
                ),
                widget.CPU(
                    background=catppuccin_mocha['base'],
                    foreground=catppuccin_mocha['text'],
                    format=' {freq_current}GHz {load_percent}%',
                ),
                widget.TextBox(
                    text='|',
                    background=catppuccin_mocha['base'],
                    foreground=catppuccin_mocha['text'],
                    padding=2,
                    fontsize=14,
                ),
                widget.TextBox(
                    '',
                    background=catppuccin_mocha['base'],
                    foreground=catppuccin_mocha['text'],
                    fontsize=16,
                ),
                widget.DF(
                    visible_on_warn=False,
                    background=catppuccin_mocha['base'],
                    foreground=catppuccin_mocha['text'],
                ),
                widget.TextBox(
                    text='|',
                    background=catppuccin_mocha['base'],
                    foreground=catppuccin_mocha['text'],
                    padding=2,
                    fontsize=14,
                ),
                widget.TextBox(
                    '',
                    background=catppuccin_mocha['base'],
                    foreground=catppuccin_mocha['text'],
                    fontsize=22,
                ),
                widget.Net(
                    background=catppuccin_mocha['base'],
                    foreground=catppuccin_mocha['text'],
                ),
                widget.TextBox(
                    text='|',
                    background=catppuccin_mocha['base'],
                    foreground=catppuccin_mocha['text'],
                    padding=2,
                    fontsize=14,
                ),
                widget.Systray(),
                widget.TextBox(
                    text='|',
                    background=catppuccin_mocha['base'],
                    foreground=catppuccin_mocha['text'],
                    padding=2,
                    fontsize=14,
                ),
                widget.KeyboardLayout(
                    foreground=catppuccin_mocha['text'],
                    background=catppuccin_mocha['base'],
                    fmt='Keyboard: {}',
                    configured_keyboard=['us altgr-intl'],
                    padding=2,
                ),
                widget.TextBox(
                    text='|',
                    background=catppuccin_mocha['base'],
                    foreground=catppuccin_mocha['text'],
                    padding=2,
                    fontsize=14,
                ),
                widget.TextBox(
                    '',
                    background=catppuccin_mocha['base'],
                    foreground=catppuccin_mocha['text'],
                    fontsize=22,
                ),
                widget.Volume(
                    background=catppuccin_mocha['base'],
                    foreground=catppuccin_mocha['text'],
                ),
                widget.TextBox(
                    text='|',
                    background=catppuccin_mocha['base'],
                    foreground=catppuccin_mocha['text'],
                    padding=2,
                    fontsize=14,
                ),
                widget.Clock(
                    format='%Y-%m-%d %a %H:%M ',
                    background=catppuccin_mocha['base'],
                    foreground=catppuccin_mocha['text'],
                ),
                widget.TextBox(
                    text='|',
                    background=catppuccin_mocha['base'],
                    foreground=catppuccin_mocha['text'],
                    padding=2,
                    fontsize=14,
                ),
                widget.QuickExit(
                    background=catppuccin_mocha['base'],
                    foreground=catppuccin_mocha['text'],
                ),
                widget.Sep(
                    linewidth=0,
                    padding=6,
                    foreground=catppuccin_mocha['text'],
                    background=catppuccin_mocha['base'],
                ),
            ],
            24,
            background=catppuccin_mocha['base'],
        ),
    ),
    Screen(
        top=bar.Bar(
            [
                widget.CurrentLayout(),
                widget.GroupBox(),
                widget.Prompt(),
                widget.WindowName(),
                widget.Chord(
                    chords_colors={
                        'launch': ('#ff0000', '#ffffff'),
                    },
                    name_transform=lambda name: name.upper(),
                ),
                widget.TextBox('default config', name='default'),
                widget.TextBox(
                    'Press &lt;M-r&gt; to spawn', foreground='#d75f5f'
                ),
                widget.Systray(),
                widget.Clock(format='%Y-%m-%d %a %I:%M %p'),
                widget.QuickExit(),
            ],
            24,
            # border_width=[2, 0, 2, 0],  # Draw top and bottom borders
            # border_color=["ff00ff", "000000", "ff00ff", "000000"]  # Borders
            # are magenta
        ),
    ),
]

# Drag floating layouts.
mouse = [
    Drag(
        [mod],
        'Button1',
        lazy.window.set_position_floating(),
        start=lazy.window.get_position(),
    ),
    Drag(
        [mod],
        'Button3',
        lazy.window.set_size_floating(),
        start=lazy.window.get_size(),
    ),
    Click([mod], 'Button2', lazy.window.bring_to_front()),
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: list
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False
floating_layout = layout.Floating(
    float_rules=[
        # Run the utility of `xprop` to see the wm class and name of an X
        # client.
        *layout.Floating.default_float_rules,
        Match(wm_class='confirmreset'),  # gitk
        Match(wm_class='makebranch'),  # gitk
        Match(wm_class='maketag'),  # gitk
        Match(wm_class='ssh-askpass'),  # ssh-askpass
        Match(title='branchdialog'),  # gitk
        Match(title='pinentry'),  # GPG key password entry
    ]
)
auto_fullscreen = True
focus_on_window_activation = 'smart'
reconfigure_screens = True

# If things like steam games want to auto-minimize themselves when losing
# focus, should we respect this or not?
auto_minimize = False

# When using the Wayland backend, this can be used to configure input devices.
wl_input_rules = None

# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = 'LG3D'
