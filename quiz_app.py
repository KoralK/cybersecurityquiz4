import streamlit as st

def main():
    st.title("Vulnerability Assessment Solutions and Tools Quiz")
    st.markdown("This quiz will test your understanding of vulnerability assessment solutions, approaches, scoring systems, and tools. By the end of this quiz, you'll be familiar with different types of vulnerability assessment solutions, how vulnerability is scored and how different approaches are used for assessments.")

    questions = [
        {
            "question": "What is the key difference between product-based and service-based vulnerability solutions?",
            "options": [
                "Product-based solutions are always cloud-based, while service-based are on-premise.",
                "Product-based solutions are normally used for external networks, while service-based are for internal.",
                 "Product-based solutions are deployed within an organization's network, while service-based solutions are provided by a third-party.",
                "Product-based solutions focus on automated scans, while service-based use manual assessments."
            ],
            "answer": "Product-based solutions are deployed within an organization's network, while service-based solutions are provided by a third-party.",
            "explanation": "Product-based solutions are deployed within the organization, whereas service-based are third-party and can be on premise or cloud based."
        },
        {
            "question": "What is a tree-based vulnerability assessment approach?",
            "options": [
                "An assessment based on an inventory of network protocols.",
                "An assessment based on cloud services.",
                 "An assessment tailored based on the types of live machines on the network.",
                "An assessment focused on network speed."
            ],
            "answer": "An assessment tailored based on the types of live machines on the network.",
            "explanation": "A tree-based assessment is when the approach is tailored based on the live machines that are on the network."
        },
         {
            "question": "What is an inference-based vulnerability assessment approach?",
            "options": [
                "An approach tailored based on the live machines that are on the network.",
                "An approach based on a specific time of day.",
                "An approach based on a specific location.",
                "An approach based on an inventory of network protocols."
            ],
            "answer": "An approach based on an inventory of network protocols.",
            "explanation": "An inference-based assessment approach is when the assessment is based on the inventory of network protocols."
         },
        {
             "question": "What is a key best practice when using vulnerability assessment tools?",
             "options": [
                "Always scan the entire network to ensure all areas are covered",
                "Scan a large range of IP addresses to make sure nothing is missed",
                 "Understand the complete functionality of the tool before starting it on the network.",
                 "Run scans at a limited number of times to reduce network load"
            ],
             "answer":"Understand the complete functionality of the tool before starting it on the network.",
             "explanation": "It is important to understand the functionality of the tool to ensure it doesn't cause unwanted damage, render services unavailable, or cause unintentional disruption."
        },
         {
             "question": "What is the purpose of the Common Vulnerability Scoring System (CVSS)?",
             "options": [
                "To assign a letter grade to each vulnerability",
                "To describe the characteristics of a network.",
                "To translate into a score reflecting vulnerability severity",
                "To create a list of potential vulnerabilities"
           ],
            "answer": "To translate into a score reflecting vulnerability severity",
            "explanation": "The CVSS translates into a numerical value for severity which can be translated to qualitative representation such as Low, Medium, High or Critical."
         },
         {
           "question": "What is the severity level associated with a CVSS base score of 9.5?",
           "options": [
               "Low",
               "Medium",
               "High",
               "Critical"
            ],
           "answer": "Critical",
           "explanation": "A CVSS base score between 9.0 and 10.0 is associated with Critical severity."
        },
          {
            "question": "What is the CVE system primarily used for?",
             "options": [
                "To assess network bandwidth.",
                 "To maintain a list of known vulnerabilities.",
                "To manage network devices.",
                "To assess user permissions."
            ],
            "answer": "To maintain a list of known vulnerabilities.",
            "explanation": "The CVE system maintains a list of known vulnerabilities, including ID number and description of each."
         },
          {
            "question": "Which US agency launched the National Vulnerability Database (NVD)?",
             "options": [
                "FBI",
                 "NIST",
                "CIA",
                "NSA"
            ],
             "answer": "NIST",
             "explanation": "The National Vulnerability Database (NVD) was launched by the National Institute of Standards and Technology (NIST)."
        },
        {
            "question": "What are vulnerability scanners primarily developed to detect?",
            "options": [
                 "Weaknesses, problems, and loopholes in an operating system",
                "Internal network traffic flow.",
                "Device specifications.",
                 "Application version numbers."
            ],
             "answer": "Weaknesses, problems, and loopholes in an operating system",
            "explanation":"Vulnerability scanners are developed to detect vulnerabilities, weaknesses, problems, and loopholes in an operating system."
        },
        {
            "question": "Which of the following is a common vulnerability scanning tool?",
            "options": [
               "Microsoft Word",
                "Nessus",
                "Zoom",
                "Adobe Photoshop"
            ],
            "answer": "Nessus",
            "explanation":"Nessus is a common vulnerability scanning tool."
         }
    ]


    if 'score' not in st.session_state:
        st.session_state.score = 0

    for i, q in enumerate(questions):
        st.subheader(f"Question {i+1}:")
        st.write(q["question"])
        selected_option = st.radio(f"Select an option:", q["options"], key=f"q{i}", index=None)

        if st.button("Check Answer", key=f"btn{i}"):
            if selected_option == q["answer"]:
                st.session_state.score += 1
                st.success("Correct!")
            elif selected_option is not None:
                st.error(f"Incorrect. The correct answer is: {q['answer']}")
            
            if selected_option is not None:
              with st.expander("Explanation"):
                st.write(q["explanation"])
            st.write("---")

    st.header("Quiz Results")
    st.write(f"Your final score is: {st.session_state.score}/{len(questions)}")

if __name__ == "__main__":
    main()