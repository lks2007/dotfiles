# Dotfiles
## Install i3
```sh 
sudo pacman -S i3
```
Then, copy i3 folder to ~/.config
![](https://i.imgur.com/xr5Qshg.png)

## Install VsCode
```sh 
sudo pacman -S code
```
Copy folder 'Code - OSS' to ~/.config
![](https://i.imgur.com/MybyY0k.png)
## Install Polybar
```sh 
sudo pacman -S polybar
```
Then, copy polybar folder to ~/.config

![](https://i.imgur.com/LsOGk4h.jpg)

## Install Neovim
```sh 
sudo pacman -S neovim
```
Now, make link with .vimrc 
```sh
ln -s ~/.vimrc ~/.config/nvim/init.vim 
```

``` sh
curl -fLo ~/.local/share/nvim/site/autoload/plug.vim --create-dirs \
    https://raw.githubusercontent.com/junegunn/vim-plug/master/plug.vim
```

Now, go to ~/.config/nvim/init.vim with nvim and do ```:PlugInstall ```

![](https://i.imgur.com/lxxuoHY.png)
