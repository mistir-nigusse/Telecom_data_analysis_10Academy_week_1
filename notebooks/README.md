
### Some of the functions available in the notebooks and codes in this repository

#### Slack Data Parsing Functions
`slack_parser`: Parses Slack data to extract relevant information such as message type, content, sender details, thread information, etc. Combines data from multiple JSON files and returns a DataFrame.

`parse_slack_reaction`: Retrieves reaction-related information from Slack data, including reaction name, count, users, associated message, and user ID. Returns a DataFrame.

`convert_2_timestamp`: Converts Unix time to a readable timestamp for specified columns in the DataFrame.

#### User Interaction and Community Analysis Functions
`get_tagged_users`: Extracts all user mentions (@) from messages.

`get_community_participation`: Analyzes community participation by counting the number of replies for each user.

`map_userid_2_realname`: Maps Slack IDs to real names using user profiles. Optionally, plots a bar graph of message counts for each user.

`get_top_20_user`: Plots the top 20 message senders in a specified channel.

`draw_avg_reply_count`: Plots the average number of reply counts per sender in a channel.

`draw_avg_reply_users_count`: Plots the average number of reply user counts per sender in a channel.

`draw_wordcloud`: Generates and displays a word cloud visualization for message content.

`draw_user_reaction`: Plots users with the most reactions in a channel.

#### Data Analysis and Visualization
`get_top_20_user(dfall_week, channel='All learning')`: Visualizes the top 20 message senders.

`draw_avg_reply_count(dfall_week, channel='All Learning')`: Visualizes the average reply count per sender.

`draw_avg_reply_users_count(dfall_week, channel='All learning')`: Visualizes the average reply user count per sender.

`draw_wordcloud(dfall_week['msg_content'], week='All Learning Week')`: Displays a word cloud for message content.

`draw_user_reaction`: Plots users with the most reactions.

