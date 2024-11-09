import streamlit as st

def main():
    st.set_page_config(page_title="AI Coding Tools Directory", layout="wide")
    
    st.title("🤖 AI Coding Tools Directory")
    st.write("A curated collection of AI-powered coding tools and assistants")

    # Sidebar for navigation
    st.sidebar.title("Categories")
    category = st.sidebar.radio(
        "Select a category",
        ["All Tools", "Web-based Assistants", "IDE Plugins", "Platform Tools"]
    )

    # Define tool data
    tools = {
        "Web-based Assistants": [
            {
                "name": "Safurai",
                "url": "https://www.safurai.com/",
                "description": "AI-powered code assistant for developers",
                "icon": "💻"
            },
            {
                "name": "GitFluence",
                "url": "https://www.gitfluence.com/",
                "description": "AI-powered Git and code analysis tool",
                "icon": "🔍"
            },
            {
                "name": "DeepAI Chat",
                "url": "https://deepai.org/chat",
                "description": "AI chat interface for coding assistance",
                "icon": "💬"
            }
        ],
        "IDE Plugins": [
            {
                "name": "AskCodi",
                "url": "https://askcodi.com/pricing",
                "description": "AI coding assistant plugin",
                "icon": "🔌"
            },
            {
                "name": "Codeium",
                "url": "https://codeium.com/",
                "description": "AI code completion and assistance",
                "icon": "⚡"
            },
            {
                "name": "Sourcegraph Cody",
                "url": "https://sourcegraph.com/cody",
                "description": "AI-powered code search and understanding",
                "icon": "🔎"
            }
        ],
        "Platform Tools": [
            {
                "name": "Replit Ghostwriter",
                "url": "https://replit.com/learn/intro-to-ghostwriter",
                "description": "AI pair programmer in Replit",
                "icon": "👻"
            },
            {
                "name": "Android Studio with Gemini",
                "url": "https://developer.android.com/studio/preview/gemini",
                "description": "AI features in Android Studio",
                "icon": "🤖"
            },
            {
                "name": "OpenAI Codex",
                "url": "https://openai.com/index/openai-codex/",
                "description": "AI system that translates natural language to code",
                "icon": "🧠"
            },
            {
                "name": "OpenAI API",
                "url": "https://platform.openai.com/docs/quickstart",
                "description": "OpenAI's API for AI-powered development",
                "icon": "🔧"
            },
            {
                "name": "Sourcegraph",
                "url": "https://sourcegraph.com/pricing",
                "description": "Code search and intelligence platform",
                "icon": "🔍"
            }
        ]
    }

    # Display tools based on selected category
    if category == "All Tools":
        for cat, tools_list in tools.items():
            st.header(f"{cat}")
            cols = st.columns(3)
            for i, tool in enumerate(tools_list):
                with cols[i % 3]:
                    with st.container():
                        st.markdown(
                            f"""
                            <div style='
                                background-color: #f0f2f6;
                                padding: 20px;
                                border-radius: 10px;
                                margin: 10px 0;
                                height: 200px;
                            '>
                                <h3>{tool['icon']} {tool['name']}</h3>
                                <p>{tool['description']}</p>
                                <br>
                                <a href='{tool['url']}' target='_blank'>
                                    <button style='
                                        background-color: #ff4b4b;
                                        color: white;
                                        padding: 10px 20px;
                                        border: none;
                                        border-radius: 5px;
                                        cursor: pointer;
                                    '>
                                        Visit Website
                                    </button>
                                </a>
                            </div>
                            """,
                            unsafe_allow_html=True
                        )
    else:
        cols = st.columns(3)
        for i, tool in enumerate(tools[category]):
            with cols[i % 3]:
                with st.container():
                    st.markdown(
                        f"""
                        <div style='
                            background-color: #f0f2f6;
                            padding: 20px;
                            border-radius: 10px;
                            margin: 10px 0;
                            height: 200px;
                        '>
                            <h3>{tool['icon']} {tool['name']}</h3>
                            <p>{tool['description']}</p>
                            <br>
                            <a href='{tool['url']}' target='_blank'>
                                <button style='
                                    background-color: #ff4b4b;
                                    color: white;
                                    padding: 10px 20px;
                                    border: none;
                                    border-radius: 5px;
                                    cursor: pointer;
                                '>
                                    Visit Website
                                </button>
                            </a>
                        </div>
                        """,
                        unsafe_allow_html=True
                    )

    # Footer
    st.markdown("---")
    st.markdown(
        "Made with ❤️ using Streamlit | "
        "Tools are organized into categories for easy navigation"
    )

if __name__ == "__main__":
    main()
