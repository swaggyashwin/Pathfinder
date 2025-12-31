import streamlit as st
import json
from typing import Dict, List, Optional
from datetime import datetime
import time
import random

# ============================================================================
# CONFIGURATION AND SETUP
# ============================================================================

st.set_page_config(
    page_title="PathFinder AI - Career Roadmap Builder",
    page_icon="🎯",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ============================================================================
# CUSTOM STYLING
# ============================================================================

def apply_custom_css():
    """Apply comprehensive custom CSS styling"""
    st.markdown("""
        <style>
        .main {
            padding: 2rem;
            background-color: #f8f9fa;
        }
        
        .stChatMessage {
            padding: 1.2rem;
            border-radius: 10px;
            margin-bottom: 1rem;
            box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        }
        
        h1 {
            color: #1a1a1a;
            font-weight: 700;
            font-size: 2.5rem;
        }
        
        h2 {
            color: #333333;
            font-weight: 600;
            font-size: 1.8rem;
        }
        
        h3 {
            color: #0066cc;
            font-weight: 600;
            font-size: 1.4rem;
        }
        
        .priority-essential {
            color: #d32f2f;
            font-weight: 700;
            background-color: #ffebee;
            padding: 0.3rem 0.6rem;
            border-radius: 5px;
        }
        
        .priority-recommended {
            color: #1976d2;
            font-weight: 600;
            background-color: #e3f2fd;
            padding: 0.3rem 0.6rem;
            border-radius: 5px;
        }
        
        .priority-optional {
            color: #757575;
            font-weight: 500;
            background-color: #f5f5f5;
            padding: 0.3rem 0.6rem;
            border-radius: 5px;
        }
        
        .skill-tag {
            display: inline-block;
            background-color: #e3f2fd;
            color: #1976d2;
            padding: 0.4rem 0.8rem;
            margin: 0.2rem;
            border-radius: 20px;
            font-size: 0.9rem;
        }
        
        .resource-item {
            padding: 0.8rem;
            margin: 0.5rem 0;
            background-color: #fafafa;
            border-radius: 8px;
            border-left: 3px solid #0066cc;
        }
        </style>
    """, unsafe_allow_html=True)

# ============================================================================
# SESSION STATE
# ============================================================================

def initialize_session_state():
    """Initialize all session state variables"""
    if "messages" not in st.session_state:
        st.session_state.messages = []
    
    if "roadmap" not in st.session_state:
        st.session_state.roadmap = None
    
    if "conversation_id" not in st.session_state:
        st.session_state.conversation_id = datetime.now().strftime("%Y%m%d_%H%M%S")
    
    if "roadmap_history" not in st.session_state:
        st.session_state.roadmap_history = []

# ============================================================================
# MOCK DATA GENERATOR
# ============================================================================

class MockDataGenerator:
    """Generates mock roadmaps for demo mode"""
    
    @staticmethod
    def generate_mock_roadmap(user_input: str) -> Dict:
        """Generate a mock roadmap based on user input"""
        time.sleep(1)  # Simulate API delay
        
        # Extract career goal from input
        career_goal = "Data Scientist"
        if "ux" in user_input.lower() or "design" in user_input.lower():
            career_goal = "UX Designer"
        elif "full stack" in user_input.lower() or "web dev" in user_input.lower():
            career_goal = "Full Stack Developer"
        elif "cloud" in user_input.lower():
            career_goal = "Cloud Architect"
        elif "machine learning" in user_input.lower() or "ml" in user_input.lower():
            career_goal = "Machine Learning Engineer"
        elif "data" in user_input.lower():
            career_goal = "Data Scientist"
        elif "cyber" in user_input.lower() or "security" in user_input.lower():
            career_goal = "Cybersecurity Analyst"
        elif "product manager" in user_input.lower() or "pm" in user_input.lower():
            career_goal = "Product Manager"
        
        return {
            "career_goal": career_goal,
            "current_level": "Beginner with basic programming knowledge",
            "target_level": "Professional-level " + career_goal,
            "estimated_timeline": "12-18 months",
            "difficulty": "Intermediate",
            "overview": f"This roadmap will guide you through becoming a {career_goal}. You'll progress from foundational concepts to advanced techniques, building a portfolio of real-world projects along the way.",
            "phases": [
                {
                    "phase_id": 1,
                    "title": "Foundations & Fundamentals",
                    "description": "Build a strong foundation in core concepts and tools",
                    "duration": "3-4 months",
                    "prerequisites": [],
                    "objectives": [
                        "Master programming fundamentals",
                        "Understand data structures and algorithms",
                        "Learn version control and development workflows"
                    ],
                    "skills": ["Python", "Git", "SQL", "Linux Basics", "Data Structures"],
                    "resources": [
                        {
                            "name": "Python for Everybody Specialization",
                            "type": "Course",
                            "description": "Comprehensive Python programming course covering basics to data structures",
                            "url": "self-guided",
                            "priority": "Essential"
                        },
                        {
                            "name": "LeetCode Easy Problems",
                            "type": "Project",
                            "description": "Practice 50+ easy algorithm problems to build problem-solving skills",
                            "url": "self-guided",
                            "priority": "Essential"
                        },
                        {
                            "name": "Git and GitHub for Beginners",
                            "type": "Course",
                            "description": "Learn version control essentials",
                            "url": "self-guided",
                            "priority": "Recommended"
                        }
                    ],
                    "milestones": [
                        "Complete 50 coding problems",
                        "Build 3 small Python projects",
                        "Create GitHub portfolio"
                    ],
                    "projects": [
                        "Personal budget tracker CLI application",
                        "Web scraper for job listings",
                        "Data analysis script for CSV files"
                    ]
                },
                {
                    "phase_id": 2,
                    "title": "Core Technical Skills",
                    "description": "Develop specialized technical competencies",
                    "duration": "4-5 months",
                    "prerequisites": ["Phase 1 completion"],
                    "objectives": [
                        "Master key frameworks and libraries",
                        "Build end-to-end projects",
                        "Understand industry best practices"
                    ],
                    "skills": ["pandas", "NumPy", "Scikit-learn", "TensorFlow", "Data Visualization"],
                    "resources": [
                        {
                            "name": "Applied Data Science with Python",
                            "type": "Course",
                            "description": "Michigan University's comprehensive data science specialization",
                            "url": "self-guided",
                            "priority": "Essential"
                        },
                        {
                            "name": "Machine Learning by Andrew Ng",
                            "type": "Course",
                            "description": "Foundational ML course covering algorithms and theory",
                            "url": "self-guided",
                            "priority": "Essential"
                        },
                        {
                            "name": "Kaggle Competitions (Beginner)",
                            "type": "Project",
                            "description": "Participate in 2-3 beginner-friendly competitions",
                            "url": "self-guided",
                            "priority": "Recommended"
                        }
                    ],
                    "milestones": [
                        "Complete 3 end-to-end ML projects",
                        "Achieve top 50% in a Kaggle competition",
                        "Build a personal portfolio website"
                    ],
                    "projects": [
                        "Customer churn prediction model",
                        "Sentiment analysis of product reviews",
                        "Housing price prediction with feature engineering"
                    ]
                },
                {
                    "phase_id": 3,
                    "title": "Advanced Topics & Specialization",
                    "description": "Deep dive into advanced concepts and choose specialization",
                    "duration": "3-4 months",
                    "prerequisites": ["Phase 2 completion"],
                    "objectives": [
                        "Master advanced ML/DL techniques",
                        "Develop specialization expertise",
                        "Build production-ready solutions"
                    ],
                    "skills": ["Deep Learning", "NLP", "Computer Vision", "MLOps", "Cloud Deployment"],
                    "resources": [
                        {
                            "name": "Deep Learning Specialization",
                            "type": "Course",
                            "description": "Andrew Ng's advanced deep learning course series",
                            "url": "self-guided",
                            "priority": "Essential"
                        },
                        {
                            "name": "Full Stack Deep Learning",
                            "type": "Course",
                            "description": "Learn to deploy ML models in production",
                            "url": "self-guided",
                            "priority": "Recommended"
                        }
                    ],
                    "milestones": [
                        "Deploy ML model to cloud",
                        "Contribute to open source ML project",
                        "Write technical blog posts"
                    ],
                    "projects": [
                        "Real-time object detection system",
                        "Chatbot with NLP capabilities",
                        "Recommendation engine with collaborative filtering"
                    ]
                },
                {
                    "phase_id": 4,
                    "title": "Professional Development & Job Search",
                    "description": "Prepare for job market and build professional presence",
                    "duration": "2-3 months",
                    "prerequisites": ["Phase 3 completion"],
                    "objectives": [
                        "Build professional network",
                        "Optimize portfolio and resume",
                        "Practice technical interviews",
                        "Apply to target companies"
                    ],
                    "skills": ["System Design", "Behavioral Interviews", "Salary Negotiation", "Networking"],
                    "resources": [
                        {
                            "name": "Cracking the Coding Interview",
                            "type": "Book",
                            "description": "Master technical interview preparation",
                            "url": "self-guided",
                            "priority": "Essential"
                        },
                        {
                            "name": "Mock Interviews",
                            "type": "Project",
                            "description": "Complete 10+ mock technical interviews",
                            "url": "self-guided",
                            "priority": "Essential"
                        }
                    ],
                    "milestones": [
                        "Apply to 50+ relevant positions",
                        "Get 5+ interview calls",
                        "Receive job offer"
                    ],
                    "projects": [
                        "Polished GitHub portfolio with documentation",
                        "Personal website with case studies",
                        "Technical blog with 5+ articles"
                    ]
                }
            ],
            "key_technologies": ["Python", "TensorFlow", "PyTorch", "SQL", "AWS/GCP", "Docker", "Git"],
            "career_paths": [
                "Data Scientist at tech company",
                "ML Engineer in fintech",
                "Research Scientist in AI lab",
                "Data Science Consultant"
            ],
            "salary_range": "$80,000 - $150,000 (entry to mid-level)",
            "industry_demand": "Very High - Data science roles are projected to grow 36% through 2031, much faster than average.",
            "required_certifications": [
                "AWS Certified Machine Learning - Specialty (Optional)",
                "TensorFlow Developer Certificate (Recommended)",
                "Google Professional Data Engineer (Optional)"
            ],
            "networking_tips": [
                "Attend local data science meetups and conferences",
                "Join online communities (Kaggle, r/datascience, MLOps community)",
                "Connect with data scientists on LinkedIn",
                "Contribute to open source ML projects",
                "Share your learning journey on social media"
            ],
            "success_metrics": [
                "Complete all 4 phases within timeline",
                "Build 10+ portfolio projects",
                "Achieve competitive Kaggle ranking",
                "Publish 5+ technical articles",
                "Receive job offers from target companies"
            ]
        }
    
    @staticmethod
    def generate_mock_response(user_input: str) -> str:
        """Generate mock conversational response"""
        time.sleep(0.5)
        
        msg_count = len(st.session_state.messages)
        has_skills = any(word in user_input.lower() for word in ["know", "experience", "familiar", "python", "html", "css", "marketing"])
        
        if msg_count == 0:
            return "Hello! I'm PathFinder AI, your career development advisor. I'd love to help you create a personalized roadmap to achieve your career goals. What role are you interested in pursuing?"
        elif msg_count == 1 and not has_skills:
            return "That sounds like an exciting career goal! To create the best roadmap for you, could you tell me about your current background? What skills or experience do you already have?"
        elif has_skills and msg_count <= 3:
            return "Perfect! Based on what you've shared, I have enough information to create a comprehensive roadmap for you. I'll generate a detailed plan with learning phases, resources, projects, and milestones. Would you like me to create your personalized career development plan now? Just say 'yes' or 'create my roadmap'!"
        else:
            responses = [
                "That's great! I can definitely help you with that. What's your target timeline for this career transition?",
                "Excellent background! That will definitely help you in your journey. Are you looking for a full-time transition or learning part-time while working?",
                "I understand. Let me know when you're ready and I'll generate your complete roadmap with all the details you need!",
            ]
            return random.choice(responses)

# ============================================================================
# INTENT DETECTOR
# ============================================================================

class IntentDetector:
    """Detects user intent for roadmap generation"""
    
    CAREER_KEYWORDS = ["want to be", "become", "transition", "switch", "career", "learn", "study", "roadmap", "help me", "guide me"]
    ROLES = ["engineer", "developer", "designer", "analyst", "scientist", "manager", "photographer", "writer", "marketer"]
    GENERATE_TRIGGERS = ["yes", "create", "generate", "make", "build", "ready", "go ahead", "let's do it", "sounds good"]
    
    @staticmethod
    def should_generate(user_input: str, history: List[Dict]) -> bool:
        """Determine if roadmap should be generated"""
        lower = user_input.lower()
        
        # Check for explicit generation request
        if any(trigger in lower for trigger in IntentDetector.GENERATE_TRIGGERS):
            all_msgs = " ".join([m["content"] for m in history if m["role"] == "user"])
            if any(k in all_msgs.lower() for k in IntentDetector.CAREER_KEYWORDS) or \
               any(r in all_msgs.lower() for r in IntentDetector.ROLES):
                return True
        
        # Check if message contains career intent and sufficient context
        has_career = any(k in lower for k in IntentDetector.CAREER_KEYWORDS) or \
                     any(r in lower for r in IntentDetector.ROLES)
        has_context = len(user_input.split()) >= 5
        
        return has_career and has_context

# ============================================================================
# VISUALIZER
# ============================================================================

class RoadmapVisualizer:
    """Renders roadmap components"""
    
    @staticmethod
    def render_complete(roadmap: Dict):
        """Render complete roadmap"""
        # Header
        st.markdown(f"## {roadmap.get('career_goal', 'Career Roadmap')}")
        if roadmap.get('overview'):
            st.info(roadmap['overview'])
        st.markdown("---")
        
        # Metrics
        col1, col2, col3, col4 = st.columns(4)
        with col1:
            st.metric("Timeline", roadmap.get('estimated_timeline', 'N/A'))
        with col2:
            st.metric("Difficulty", roadmap.get('difficulty', 'N/A'))
        with col3:
            st.metric("Phases", len(roadmap.get('phases', [])))
        with col4:
            milestones = sum(len(p.get('milestones', [])) for p in roadmap.get('phases', []))
            st.metric("Milestones", milestones)
        
        st.markdown("---")
        
        # Overview
        if roadmap.get('current_level') or roadmap.get('target_level'):
            st.markdown("### Journey Overview")
            col1, col2 = st.columns(2)
            with col1:
                if roadmap.get('current_level'):
                    st.info(f"**Starting Point**\n\n{roadmap['current_level']}")
            with col2:
                if roadmap.get('target_level'):
                    st.success(f"**Target Level**\n\n{roadmap['target_level']}")
        
        st.markdown("---")
        
        # Key Info
        col1, col2 = st.columns(2)
        with col1:
            if roadmap.get('key_technologies'):
                st.markdown("### Core Technologies")
                for tech in roadmap['key_technologies']:
                    st.markdown(f"- {tech}")
        with col2:
            if roadmap.get('required_certifications'):
                st.markdown("### Certifications")
                for cert in roadmap['required_certifications']:
                    st.markdown(f"- {cert}")
        
        if roadmap.get('industry_demand'):
            st.markdown("### Market Insights")
            st.write(roadmap['industry_demand'])
        
        if roadmap.get('salary_range'):
            st.markdown("### Salary Range")
            st.write(roadmap['salary_range'])
        
        st.markdown("---")
        
        # Learning Phases
        st.markdown("## Learning Phases")
        total = len(roadmap.get('phases', []))
        for i, phase in enumerate(roadmap.get('phases', []), 1):
            progress = (i / total) * 100
            
            with st.expander(f"Phase {phase.get('phase_id', i)}: {phase.get('title', 'Phase')}", expanded=(i == 1)):
                st.progress(progress / 100)
                st.caption(f"Phase {i} of {total}")
                
                st.markdown("**Description**")
                st.write(phase.get('description', ''))
                
                col1, col2 = st.columns(2)
                with col1:
                    if phase.get('duration'):
                        st.markdown(f"**Duration:** {phase['duration']}")
                with col2:
                    st.markdown(f"**Skills:** {len(phase.get('skills', []))}")
                
                if phase.get('objectives'):
                    st.markdown("**Objectives**")
                    for j, obj in enumerate(phase['objectives'], 1):
                        st.markdown(f"{j}. {obj}")
                
                if phase.get('skills'):
                    st.markdown("**Skills**")
                    html = " ".join([f'<span class="skill-tag">{s}</span>' for s in phase['skills']])
                    st.markdown(html, unsafe_allow_html=True)
                
                if phase.get('resources'):
                    st.markdown("**Resources**")
                    for r in phase['resources']:
                        priority = r.get('priority', 'Optional')
                        classes = {'Essential': 'priority-essential', 'Recommended': 'priority-recommended', 'Optional': 'priority-optional'}
                        html = f"""
                        <div class="resource-item">
                            <span class="{classes.get(priority, '')}">[{priority.upper()}]</span>
                            <strong>{r.get('name', 'Resource')}</strong> ({r.get('type', 'Resource')})
                            <br><small>{r.get('description', '')}</small>
                        </div>
                        """
                        st.markdown(html, unsafe_allow_html=True)
                
                if phase.get('projects'):
                    st.markdown("**Projects**")
                    for j, proj in enumerate(phase['projects'], 1):
                        st.markdown(f"{j}. {proj}")
                
                if phase.get('milestones'):
                    st.markdown("**Milestones**")
                    for j, m in enumerate(phase['milestones'], 1):
                        st.checkbox(m, key=f"m_{phase.get('phase_id', i)}_{j}")
        
        st.markdown("---")
        
        # Additional
        col1, col2 = st.columns(2)
        with col1:
            if roadmap.get('career_paths'):
                st.markdown("### Career Paths")
                for i, path in enumerate(roadmap['career_paths'], 1):
                    st.markdown(f"{i}. {path}")
        with col2:
            if roadmap.get('networking_tips'):
                st.markdown("### Networking")
                for tip in roadmap['networking_tips']:
                    st.markdown(f"- {tip}")
        
        if roadmap.get('success_metrics'):
            st.markdown("### Success Metrics")
            for metric in roadmap['success_metrics']:
                st.markdown(f"- {metric}")

# ============================================================================
# SIDEBAR
# ============================================================================

def render_sidebar():
    """Render sidebar"""
    with st.sidebar:
        st.title("PathFinder AI")
        st.caption("Career Development Platform")
        st.markdown("---")
        
        st.success("🎮 Demo Mode Active")
        st.caption("Using mock data (100% FREE!)")
        
        st.markdown("---")
        st.subheader("About")
        st.info("""
        PathFinder AI creates personalized career roadmaps using AI.
        
        **Features:**
        - Customized learning paths
        - Industry insights
        - Resource recommendations
        - Progress tracking
        """)
        
        st.markdown("---")
        
        st.subheader("Quick Actions")
        if st.button("New Roadmap", use_container_width=True):
            st.session_state.roadmap = None
            st.session_state.messages = []
            st.rerun()
        
        if st.session_state.get('roadmap'):
            if st.button("Export JSON", use_container_width=True):
                json_str = json.dumps(st.session_state.roadmap, indent=2)
                st.download_button(
                    "Download",
                    json_str,
                    f"roadmap_{st.session_state.conversation_id}.json",
                    "application/json",
                    use_container_width=True
                )
        
        st.markdown("---")
        st.caption("Powered by AI • Demo Mode")

# ============================================================================
# MAIN APPLICATION
# ============================================================================

def main():
    """Main application"""
    apply_custom_css()
    initialize_session_state()
    render_sidebar()
    
    st.title("PathFinder AI")
    st.markdown("### Career Roadmap Builder")
    st.caption("Build your personalized career development plan with AI")
    st.markdown("---")
    
    col1, col2 = st.columns([1, 1])
    
    # LEFT: Chat
    with col1:
        st.subheader("Career Advisor Chat")
        
        for msg in st.session_state.messages:
            with st.chat_message(msg["role"]):
                st.write(msg["content"])
        
        if prompt := st.chat_input("Tell me about your career goals..."):
            st.session_state.messages.append({"role": "user", "content": prompt})
            
            with st.chat_message("user"):
                st.write(prompt)
            
            with st.chat_message("assistant"):
                with st.spinner("Thinking..."):
                    if IntentDetector.should_generate(prompt, st.session_state.messages[:-1]):
                        roadmap = MockDataGenerator.generate_mock_roadmap(prompt)
                        if roadmap:
                            st.session_state.roadmap = roadmap
                            st.session_state.roadmap_history.append({"timestamp": datetime.now(), "roadmap": roadmap})
                            reply = f"✨ Created your roadmap for **{roadmap['career_goal']}**! Check the right panel to see your personalized plan."
                        else:
                            reply = "I had trouble creating your roadmap. Could you provide more details about your current skills and goals?"
                    else:
                        reply = MockDataGenerator.generate_mock_response(prompt)
                    
                    st.write(reply)
            
            st.session_state.messages.append({"role": "assistant", "content": reply})
            st.rerun()
    
    # RIGHT: Roadmap
    with col2:
        st.subheader("Your Learning Roadmap")
        
        if st.session_state.roadmap:
            RoadmapVisualizer.render_complete(st.session_state.roadmap)
        else:
            st.info("💬 Start a conversation to generate your personalized roadmap")
            
            st.markdown("### Example Queries")
            examples = [
                "I want to become a Data Scientist, I know Python and Excel",
                "Help me transition to UX Design from marketing",
                "I want to be a Full Stack Developer with HTML/CSS knowledge",
                "Guide me to become a Cloud Architect with AWS",
                "I want to learn Machine Learning, I have programming basics"
            ]
            
            for ex in examples:
                st.markdown(f"- *{ex}*")
            
            st.markdown("---")
            st.markdown("### How It Works")
            st.markdown("""
            1. 💬 Share your career goal and current skills
            2. 🤖 AI analyzes and creates your personalized roadmap
            3. 📚 Follow structured phases with resources
            4. ✅ Track progress with milestones
            5. 🎯 Achieve your career objectives
            """)

if __name__ == "__main__":
    main()