# Is-Server-Down-Discord-Notification

Check if your server is on or off for the time interval you want. Discord instant notification script.

![image](https://user-images.githubusercontent.com/38614710/106111494-1fe6bc00-615d-11eb-94b2-95ea46aa111d.png)
![image](https://user-images.githubusercontent.com/38614710/106111858-a00d2180-615d-11eb-9e98-7c6b50bdffe0.png)


### Installation

`pip install -r requirements.txt`

Then set config.json and start main.py

### Keep open for Linux background

Install screen package for linux

Then type

```
screen -S downbot
python3 main.py
```

Then press ctrl+a+d

If you want check logs , type

```
screen -r downbot
```

Then for quit press ctrl+a+d

### Config Keys Meanings

| Key          | Description                                                                         | Value Type |
| ------------ | ----------------------------------------------------------------------------------- | ---------- |
| `serverips`  | List of your ip addresses you want check                                            | array      |
| `webhookurl` | The webhook url of the channel you want to receive notifications                    | str        |
| `looptime`   | Checker refresh second                                                              | str        |
| `downmsg`    | The message to be sent to your channel when the server downs (You can add mentions) | str        |
