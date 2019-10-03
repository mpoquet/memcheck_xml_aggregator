{
  pkgs ? import (
    fetchTarball "https://github.com/NixOS/nixpkgs/archive/19.03.tar.gz") {},
}:

let
  pythonPackages = pkgs.python37Packages;
  python = pkgs.python37;

  self = rec {
    dev_shell = pkgs.mkShell {
      name = "dev-shell";
      buildInputs = [
        python
        pythonPackages.ipython
        pythonPackages.pylint
        pythonPackages.pytest
        pythonPackages.pytestcov
        pythonPackages.setuptools
        pythonPackages.wheel
        pythonPackages.pip
      ];
    };
  };
in
  self
