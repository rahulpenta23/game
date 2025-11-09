import streamlit as st
import requests

res = requests.get("https://www.freetogame.com/api/games?platform=pc")
if res.status_code == 200:
    games_data = res.json()
else:
    st.error("Failed to fetch games data.")
    st.stop()

users = [{"rahul": "123456"}]

if "logged_in" not in st.session_state:    
    st.session_state.logged_in = False

st.sidebar.title("🎮 Navigation")
page = st.sidebar.selectbox(
    "Go to:",
    ["User Access Page", "Free to Play Games on PC", "Games Online Suggestions"]
)

if page == "User Access Page":
    st.title("User Access Page")

    username = st.text_input("Reg_name", placeholder="reg_name")
    password = st.text_input("Password", type="password")

    if st.button("Login"):
        if username in users and users[username] == password:
            st.success("✅ Valid user")
            st.session_state.logged_in = True
            st.session_state.username = username
        else:
            st.error("Only authorized users can log in")
            st.button('click here to reg ')
            sarele = st.text_input('reag_name',placeholder='new')
            inkachalu = st.text_input('new_pass',placeholder='new_one',type='password')
            ss=users.append(f"{sarele}:{inkachalu}")
            print(users)

    if st.session_state.logged_in:
        st.info("✅ You are logged in. Access other pages from the sidebar.")

elif page == "Free to Play Games on PC":
    if not st.session_state.logged_in:
        st.warning("🔒 Please log in first from the User Access Page!")
    else:
        st.title("🎮 Free to Play Games on PC")

        search_query = st.text_input(
            "Search for a game",
            placeholder="🕹️ Search for a game",
            label_visibility="collapsed"
        )

        if search_query == "":
            st.info("Start typing to search for a game 🎮")
        else:
            found = False
            for game in games_data:
                if search_query.lower() in game["title"].lower():
                    found = True
                    with st.container(border=True):
                        cols1 = st.columns([3, 2])
                        with cols1[0]:
                            st.subheader(game["title"])
                            st.write("🎮 **Genre:**", game["genre"])
                            st.write("📝 **Short Description:**", game["short_description"])
                            st.write("🔗 **Profile:**", game["freetogame_profile_url"])
                            st.write("developer", game["developer"])
                            st.link_button("Play Now", game["game_url"], type="primary")
                        with cols1[1]:
                            st.image(game["thumbnail"])
            if not found:
                st.warning("No matching games found. Try a different name 🎯")

elif page == "Games Online Suggestions":
    if not st.session_state.logged_in:
        st.warning("🔒 Please log in first from the User Access Page!")
    else:
        st.title("🕹️ Games Online Suggestions")

        st.subheader("Choose your mode:")
        option = st.radio(
            "Mode:",
            ["👾 AI Recommendations", "🔥 Trending Games", "🎲 Random Picks"],
            index=1
        )
        st.write(f"Selected option is {option}")

        if option == "👾 AI Recommendations":
            st.link_button(
                "Submit",
                "https://www.jotform.com/agent/019a30429feb776495348530d8ac77a999ea",
                type="primary"
            )
        elif option == "🔥 Trending Games":
            trending_games = {
                "SmashKarts": "https://www.smashkarts.io/",
                "Super Sus": "https://supersusgame.com/",
                "UNO": "https://unoonline.io/"
            }
            st.markdown("### 🔥 Trending Games")
            for name, link in trending_games.items():
                st.link_button(name, link, type='primary')
        elif option == "🎲 Random Picks":
            st.link_button("Submit", "https://poki.com/en/popular", type="primary")
        else:
            st.info("Option not found")

        st.success("Select a mode from the sidebar to explore games! 🎮")
