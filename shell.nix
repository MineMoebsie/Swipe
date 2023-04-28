{ pkgs ? import <nixpkgs> {} }:
let
  packages = ps: with ps; [
    pygame
    numpy
  ];
  python = pkgs.python3.withPackages packages;
in pkgs.mkShell {
  buildInputs = [ python ];
}
