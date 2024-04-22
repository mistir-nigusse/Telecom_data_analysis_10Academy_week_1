{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "%reload_ext autoreload\n",
    "%autoreload 2"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "import os, sys\n",
    "import re\n",
    "import json\n",
    "import glob\n",
    "import datetime\n",
    "from collections import Counter\n",
    "\n",
    "import pandas as pd\n",
    "from matplotlib import pyplot as plt\n",
    "import seaborn as sns\n",
    "\n",
    "from nltk.corpus import stopwords\n",
    "from wordcloud import WordCloud"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Add parent directory to path to import modules from src\n",
    "rpath = os.path.abspath('..')\n",
    "if rpath not in sys.path:\n",
    "    sys.path.insert(0, rpath)\n",
    "\n",
    "from src.loader import SlackDataLoader\n",
    "import src.utils as utils"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Columns we can get from a slack message<br>\n",
    "\n",
    "message_type, message_content, sender_id, time_sent, message_distribution, time_thread_start, reply_count, reply_user_count, time_thread_end, reply_users"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "From a single slack message, we can get <br>\n",
    "\n",
    "1. The message<br>\n",
    "2. Type (message, file, link, etc)<br>\n",
    "3. The sender_id (assigned by slack)<br>\n",
    "4. The time the message was sent<br>\n",
    "5. The team (i don't know what that is now)<br>\n",
    "6. The type of the message (broadcast message, inhouse, just messgae)<br>\n",
    "7. The thread the message generated (from here we can go):<br>\n",
    "    7.1 Text/content of the message<br>\n",
    "    7.2 The thread time of the message<br>\n",
    "    7.3 The thread count (reply count)<br>\n",
    "    7.4 The number of user that reply the message (count of users that participated in the thread)<br>\n",
    "    7.5 The time the last thread message was sent <br>\n",
    "    7.6 The users that participated in the thread (their ids are stored as well)<br>"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# combine all json file in all-weeks8-9\n",
    "def slack_parser(path_channel):\n",
    "    \"\"\" parse slack data to extract useful informations from the json file\n",
    "        step of execution\n",
    "        1. Import the required modules\n",
    "        2. read all json file from the provided path\n",
    "        3. combine all json files in the provided path\n",
    "        4. extract all required informations from the slack data\n",
    "        5. convert to dataframe and merge all\n",
    "        6. reset the index and return dataframe\n",
    "    \"\"\"\n",
    "\n",
    "    # specify path to get json files\n",
    "    combined = []\n",
    "    for json_file in glob.glob(f\"{path_channel}*.json\"):\n",
    "        with open(json_file, 'r', encoding=\"utf8\") as slack_data:\n",
    "            combined.append(slack_data)\n",
    "\n",
    "    # loop through all json files and extract required informations\n",
    "    dflist = []\n",
    "    for slack_data in combined:\n",
    "\n",
    "        msg_type, msg_content, sender_id, time_msg, msg_dist, time_thread_st, reply_users, \\\n",
    "        reply_count, reply_users_count, tm_thread_end = [],[],[],[],[],[],[],[],[],[]\n",
    "\n",
    "        for row in slack_data:\n",
    "            if 'bot_id' in row.keys():\n",
    "                continue\n",
    "            else:\n",
    "                msg_type.append(row['type'])\n",
    "                msg_content.append(row['text'])\n",
    "                if 'user_profile' in row.keys(): sender_id.append(row['user_profile']['real_name'])\n",
    "                else: sender_id.append('Not provided')\n",
    "                time_msg.append(row['ts'])\n",
    "                if 'blocks' in row.keys() and len(row['blocks'][0]['elements'][0]['elements']) != 0 :\n",
    "                     msg_dist.append(row['blocks'][0]['elements'][0]['elements'][0]['type'])\n",
    "                else: msg_dist.append('reshared')\n",
    "                if 'thread_ts' in row.keys():\n",
    "                    time_thread_st.append(row['thread_ts'])\n",
    "                else:\n",
    "                    time_thread_st.append(0)\n",
    "                if 'reply_users' in row.keys(): reply_users.append(\",\".join(row['reply_users'])) \n",
    "                else:    reply_users.append(0)\n",
    "                if 'reply_count' in row.keys():\n",
    "                    reply_count.append(row['reply_count'])\n",
    "                    reply_users_count.append(row['reply_users_count'])\n",
    "                    tm_thread_end.append(row['latest_reply'])\n",
    "                else:\n",
    "                    reply_count.append(0)\n",
    "                    reply_users_count.append(0)\n",
    "                    tm_thread_end.append(0)\n",
    "        data = zip(msg_type, msg_content, sender_id, time_msg, msg_dist, time_thread_st,\n",
    "         reply_count, reply_users_count, reply_users, tm_thread_end)\n",
    "        columns = ['msg_type', 'msg_content', 'sender_name', 'msg_sent_time', 'msg_dist_type',\n",
    "         'time_thread_start', 'reply_count', 'reply_users_count', 'reply_users', 'tm_thread_end']\n",
    "\n",
    "        df = pd.DataFrame(data=data, columns=columns)\n",
    "        df = df[df['sender_name'] != 'Not provided']\n",
    "        dflist.append(df)\n",
    "\n",
    "    dfall = pd.concat(dflist, ignore_index=True)\n",
    "    dfall['channel'] = path_channel.split('/')[-1].split('.')[0]        \n",
    "    dfall = dfall.reset_index(drop=True)\n",
    "    \n",
    "    return dfall\n",
    "\n",
    "\n",
    "def parse_slack_reaction(path, channel):\n",
    "    \"\"\"get reactions\"\"\"\n",
    "    dfall_reaction = pd.DataFrame()\n",
    "    combined = []\n",
    "    for json_file in glob.glob(f\"{path}*.json\"):\n",
    "        with open(json_file, 'r') as slack_data:\n",
    "            combined.append(slack_data)\n",
    "\n",
    "    reaction_name, reaction_count, reaction_users, msg, user_id = [], [], [], [], []\n",
    "\n",
    "    for k in combined:\n",
    "        slack_data = json.load(open(k.name, 'r', encoding=\"utf-8\"))\n",
    "        \n",
    "        for i_count, i in enumerate(slack_data):\n",
    "            if 'reactions' in i.keys():\n",
    "                for j in range(len(i['reactions'])):\n",
    "                    msg.append(i['text'])\n",
    "                    user_id.append(i['user'])\n",
    "                    reaction_name.append(i['reactions'][j]['name'])\n",
    "                    reaction_count.append(i['reactions'][j]['count'])\n",
    "                    reaction_users.append(\",\".join(i['reactions'][j]['users']))\n",
    "                \n",
    "    data_reaction = zip(reaction_name, reaction_count, reaction_users, msg, user_id)\n",
    "    columns_reaction = ['reaction_name', 'reaction_count', 'reaction_users_count', 'message', 'user_id']\n",
    "    df_reaction = pd.DataFrame(data=data_reaction, columns=columns_reaction)\n",
    "    df_reaction['channel'] = channel\n",
    "    return df_reaction\n",
    "\n",
    "def get_community_participation(path):\n",
    "    \"\"\" specify path to get json files\"\"\"\n",
    "    combined = []\n",
    "    comm_dict = {}\n",
    "    for json_file in glob.glob(f\"{path}*.json\"):\n",
    "        with open(json_file, 'r') as slack_data:\n",
    "            combined.append(slack_data)\n",
    "    # print(f\"Total json files is {len(combined)}\")\n",
    "    for i in combined:\n",
    "        a = json.load(open(i.name, 'r', encoding='utf-8'))\n",
    "\n",
    "        for msg in a:\n",
    "            if 'replies' in msg.keys():\n",
    "                for i in msg['replies']:\n",
    "                    comm_dict[i['user']] = comm_dict.get(i['user'], 0)+1\n",
    "    return comm_dict"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "def convert_2_timestamp(column, data):\n",
    "    \"\"\"convert from unix time to readable timestamp\n",
    "        args: column: columns that needs to be converted to timestamp\n",
    "                data: data that has the specified column\n",
    "    \"\"\"\n",
    "    if column in data.columns.values:\n",
    "        timestamp_ = []\n",
    "        for time_unix in data[column]:\n",
    "            if time_unix == 0:\n",
    "                timestamp_.append(0)\n",
    "            else:\n",
    "                a = datetime.datetime.fromtimestamp(float(time_unix))\n",
    "                timestamp_.append(a.strftime('%Y-%m-%d %H:%M:%S'))\n",
    "        return timestamp_\n",
    "    else: \n",
    "        print(f\"{column} not in data\")\n",
    "\n",
    "def get_tagged_users(df):\n",
    "    \"\"\"get all @ in the messages\"\"\"\n",
    "\n",
    "    return df['msg_content'].map(lambda x: re.findall(r'@U\\w+', x))\n",
    "\n",
    "\n",
    "    \n",
    "def map_userid_2_realname(user_profile: dict, comm_dict: dict, plot=False):\n",
    "    \"\"\"\n",
    "    map slack_id to realnames\n",
    "    user_profile: a dictionary that contains users info such as real_names\n",
    "    comm_dict: a dictionary that contains slack_id and total_message sent by that slack_id\n",
    "    \"\"\"\n",
    "    user_dict = {} # to store the id\n",
    "    real_name = [] # to store the real name\n",
    "    ac_comm_dict = {} # to store the mapping\n",
    "    count = 0\n",
    "    # collect all the real names\n",
    "    for i in range(len(user_profile['profile'])):\n",
    "        real_name.append(dict(user_profile['profile'])[i]['real_name'])\n",
    "\n",
    "    # loop the slack ids\n",
    "    for i in user_profile['id']:\n",
    "        user_dict[i] = real_name[count]\n",
    "        count += 1\n",
    "\n",
    "    # to store mapping\n",
    "    for i in comm_dict:\n",
    "        if i in user_dict:\n",
    "            ac_comm_dict[user_dict[i]] = comm_dict[i]\n",
    "\n",
    "    ac_comm_dict = pd.DataFrame(data= zip(ac_comm_dict.keys(), ac_comm_dict.values()),\n",
    "    columns=['LearnerName', '# of Msg sent in Threads']).sort_values(by='# of Msg sent in Threads', ascending=False)\n",
    "    \n",
    "    if plot:\n",
    "        ac_comm_dict.plot.bar(figsize=(15, 7.5), x='LearnerName', y='# of Msg sent in Threads')\n",
    "        plt.title('Student based on Message sent in thread', size=20)\n",
    "        \n",
    "    return ac_comm_dict"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "def get_top_20_user(data, channel='Random'):\n",
    "    \"\"\"get user with the highest number of message sent to any channel\"\"\"\n",
    "\n",
    "    data['sender_name'].value_counts()[:20].plot.bar(figsize=(15, 7.5))\n",
    "    plt.title(f'Top 20 Message Senders in #{channel} channels', size=15, fontweight='bold')\n",
    "    plt.xlabel(\"Sender Name\", size=18); plt.ylabel(\"Frequency\", size=14);\n",
    "    plt.xticks(size=12); plt.yticks(size=12);\n",
    "    plt.show()\n",
    "\n",
    "    data['sender_name'].value_counts()[-10:].plot.bar(figsize=(15, 7.5))\n",
    "    plt.title(f'Bottom 10 Message Senders in #{channel} channels', size=15, fontweight='bold')\n",
    "    plt.xlabel(\"Sender Name\", size=18); plt.ylabel(\"Frequency\", size=14);\n",
    "    plt.xticks(size=12); plt.yticks(size=12);\n",
    "    plt.show()\n",
    "\n",
    "def draw_avg_reply_count(data, channel='Random'):\n",
    "    \"\"\"who commands many reply?\"\"\"\n",
    "\n",
    "    data.groupby('sender_name')['reply_count'].mean().sort_values(ascending=False)[:20]\\\n",
    "        .plot(kind='bar', figsize=(15,7.5));\n",
    "    plt.title(f'Average Number of reply count per Sender in #{channel}', size=20, fontweight='bold')\n",
    "    plt.xlabel(\"Sender Name\", size=18); plt.ylabel(\"Frequency\", size=18);\n",
    "    plt.xticks(size=14); plt.yticks(size=14);\n",
    "    plt.show()\n",
    "\n",
    "def draw_avg_reply_users_count(data, channel='Random'):\n",
    "    \"\"\"who commands many user reply?\"\"\"\n",
    "\n",
    "    data.groupby('sender_name')['reply_users_count'].mean().sort_values(ascending=False)[:20].plot(kind='bar',\n",
    "     figsize=(15,7.5));\n",
    "    plt.title(f'Average Number of reply user count per Sender in #{channel}', size=20, fontweight='bold')\n",
    "    plt.xlabel(\"Sender Name\", size=18); plt.ylabel(\"Frequency\", size=18);\n",
    "    plt.xticks(size=14); plt.yticks(size=14);\n",
    "    plt.show()\n",
    "\n",
    "def draw_wordcloud(msg_content, week):    \n",
    "    # word cloud visualization\n",
    "    allWords = ' '.join([twts for twts in msg_content])\n",
    "    wordCloud = WordCloud(background_color='#975429', width=500, height=300, random_state=21, max_words=500, mode='RGBA',\n",
    "                            max_font_size=140, stopwords=stopwords.words('english')).generate(allWords)\n",
    "    plt.figure(figsize=(15, 7.5))\n",
    "    plt.imshow(wordCloud, interpolation=\"bilinear\")\n",
    "    plt.axis('off')\n",
    "    plt.tight_layout()\n",
    "    plt.title(f'WordCloud for {week}', size=30)\n",
    "    plt.show()\n",
    "\n",
    "def draw_user_reaction(data, channel='General'):\n",
    "    data.groupby('sender_name')[['reply_count', 'reply_users_count']].sum()\\\n",
    "        .sort_values(by='reply_count',ascending=False)[:10].plot(kind='bar', figsize=(15, 7.5))\n",
    "    plt.title(f'User with the most reaction in #{channel}', size=25);\n",
    "    plt.xlabel(\"Sender Name\", size=18); plt.ylabel(\"Frequency\", size=18);\n",
    "    plt.xticks(size=14); plt.yticks(size=14);\n",
    "    plt.show()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Insight Extraction\n",
    "\n",
    "Below are some useful questions to answer. Feel free to explore to answer other interesting questions that may be of help to get insight about student's behaviour, need, and future performance "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# which user has the highest number of reply counts?"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Visualize reply counts per user per channel"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# what is the time range of the day that most messages are sent?\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "metadata": {},
   "outputs": [],
   "source": [
    "# what kind of messages are replied faster than others?"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Relationship between # of messages and # of reactions"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Classify messages into different categories such as questions, answers, comments, etc."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Which users got the most reactions?"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 33,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Model topics mentioned in the channel"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# What are the topics that got the most reactions?"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Harder questions to look into"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Based on messages, reactions, references shared, and other relevant data such as classification of questions into techical question, comment, answer, aorder stu the python, statistics, and sql skill level of a user?"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.6"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
