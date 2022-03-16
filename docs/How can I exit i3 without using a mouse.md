
created: 2021-07-30T17:19:47 (UTC -04:00)
tags: []
source: https://unix.stackexchange.com/questions/483934/how-can-i-exit-i3-without-using-a-mouse
author: LocoCoyoteLocoCoyote
        9111 [[silver]] badge22 bronze badges


How can I exit i3 without using a mouse? - Unix & Linux Stack Exchange

Excerpt
Whenever I go to exit i3 a bar shows up on the [[top]] giving me the ability to to click Yes, to exit, or X to cancel.


Whenever I go to exit i3 a bar shows up on the [[top]] giving me the ability to to click Yes, to exit, or X to cancel.
asked Nov 24 '18 at 22:09
[

](https://unix.stackexchange.com/users/3285/evan-carroll)
Evan CarrollEvan Carroll
19.6k28 [[gold]] badges106 [[silver]] badges184 bronze badges
Add this to your config:
```
mode "exit: [l]ogout, [r]eboot, [s]hutdown" {
bindsym l exec i3-msg exit
bindsym r exec systemctl reboot
bindsym s exec systemctl shutdown
bindsym Escape mode "default"
bindsym Return mode "default"
}
bindsym $mod+x mode "exit: [l]ogout, [r]eboot, [s]hutdown"
```
now use mod+x and then choose l, r, or s
[

](https://unix.stackexchange.com/users/4[[1754]]/4[[1754]])
4[[1754]]
811 [[gold]] badge7 [[silver]] badges19 bronze badges
answered Oct 30 '19 at 9:44
[

](https://unix.stackexchange.com/users/379693/lococoyote)
1
What you want to do is edit your i3 conf, to find out where that is out you can use i3-config-wizard,
$ i3-config-wizard
The config file "/home/$USER/.config/i3/config" already exists. Exiting.
The line that sets up the exit command is in that file, and it was created by default
bindsym $mod+Shift+e exec "i3-nagbar -t warning -m 'You pressed the exit shortcut. Do you really want to exit i3? This will end your X session.' -b 'Yes, exit i3' 'i3-msg exit'"
You'll see the i3-nagbar. That's the bar at the [[top]] responsible for nagging you. Just change that to go straight to the exit branch,
bindsym $mod+Shift+e exit
And finally run i3-msg reload to reload the configuration file.
[

](https://unix.stackexchange.com/users/321265/jaimet)
answered Nov 24 '18 at 22:09
[

](https://unix.stackexchange.com/users/3285/evan-carroll)
Evan CarrollEvan Carroll
19.6k28 [[gold]] badges106 [[silver]] badges184 bronze badges
I ran into this while wanting a way to exit i3 that was both keyboard-only and that I was unlikely to fat-finger. (Having $mod-Shift-e for exit and $mod-Shift-r for restart right next to each other is uncomfortable.) My solution is to use dmenu to run
i3 exit or i3-msg exit
In addition to being something that I can't accidentally type while trying to type something else, it has the advantages that it doesn't require any new configuration, and it reminds you how the shortcut keys work internally.
answered Jan 5 '20 at 14:33
[

](https://unix.stackexchange.com/users/389032/sam-newbold)
Not the answer you're looking for? Browse other questions tagged i3 exit or ask your own question.