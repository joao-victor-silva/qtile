{ pkgs ? import (fetchTarball "https://github.com/NixOS/nixpkgs/archive/refs/tags/22.05.tar.gz") {} }:

pkgs.mkShell {
  buildInputs = [
    pkgs.python3
    pkgs.python3.pkgs.virtualenv
    pkgs.python3.pkgs.pip
    pkgs.python3.pkgs.python-lsp-server
    pkgs.python3.pkgs.flake8
    pkgs.python3.pkgs.mypy
    pkgs.python3.pkgs.ujson
    pkgs.gitlint
    pkgs.codespell
    pkgs.nodePackages.cspell
    pkgs.gh
  ];

  shellHook = ''
    if [[ ! -r .venv/bin/activate ]]; then
      virtualenv .venv
      source .venv/bin/activate
      pip install -r requirements.txt
    else
      source .venv/bin/activate
    fi
  '';

  DIAGNOSTICS = "flake8:mypy:gitlint:cspell:codespell";
  FORMATTING = "blue";
}

