import streamlit as st
from io import BytesIO
from fpdf import FPDF

# Function to generate PDF
def generate_pdf(personal_info, education, experience, skills):
    pdf = FPDF()
    pdf.set_auto_page_break(auto=True, margin=15)
    pdf.add_page()

    # Title
    pdf.set_font('Arial', 'B', 16)
    pdf.cell(0, 10, 'Resume', ln=True, align='C')

    # Personal Information
    pdf.set_font('Arial', 'B', 12)
    pdf.cell(0, 10, 'Personal Information', ln=True)
    pdf.set_font('Arial', '', 12)
    for key, value in personal_info.items():
        pdf.cell(0, 10, f'{key}: {value}', ln=True)

    # Education
    pdf.set_font('Arial', 'B', 12)
    pdf.cell(0, 10, 'Education', ln=True)
    pdf.set_font('Arial', '', 12)
    for edu in education:
        pdf.cell(0, 10, f"{edu['Degree']} from {edu['Institution']} ({edu['Year']})", ln=True)

    # Experience
    pdf.set_font('Arial', 'B', 12)
    pdf.cell(0, 10, 'Experience', ln=True)
    pdf.set_font('Arial', '', 12)
    for exp in experience:
        pdf.cell(0, 10, f"{exp['Role']} at {exp['Company']} ({exp['Years']})", ln=True)

    # Skills
    pdf.set_font('Arial', 'B', 12)
    pdf.cell(0, 10, 'Skills', ln=True)
    pdf.set_font('Arial', '', 12)
    for skill in skills:
        pdf.cell(0, 10, skill, ln=True)

    # Save to BytesIO object
    pdf_output = BytesIO()
    pdf.output(pdf_output)
    return pdf_output

# Streamlit App
def main():
    st.title("Resume Builder")
    
    # Personal Information
    st.header("Personal Information")
    name = st.text_input("Full Name")
    email = st.text_input("Email")
    phone = st.text_input("Phone Number")
    address = st.text_area("Address")

    # Education
    st.header("Education")
    education = []
    num_education = st.number_input("Number of Educational Qualifications", min_value=1, max_value=10, step=1)
    for i in range(int(num_education)):
        degree = st.text_input(f"Degree {i+1}")
        institution = st.text_input(f"Institution {i+1}")
        year = st.text_input(f"Year of Completion {i+1}")
        education.append({"Degree": degree, "Institution": institution, "Year": year})
    
    # Experience
    st.header("Experience")
    experience = []
    num_experience = st.number_input("Number of Work Experiences", min_value=1, max_value=10, step=1)
    for i in range(int(num_experience)):
        role = st.text_input(f"Role {i+1}")
        company = st.text_input(f"Company {i+1}")
        years = st.text_input(f"Years Worked {i+1}")
        experience.append({"Role": role, "Company": company, "Years": years})

    # Skills
    st.header("Skills")
    skills = st.text_area("Enter your skills (comma separated)").split(',')

    # Generate PDF Button
    if st.button("Generate Resume"):
        personal_info = {
            "Name": name,
            "Email": email,
            "Phone": phone,
            "Address": address
        }
        
        pdf_output = generate_pdf(personal_info, education, experience, skills)
        st.download_button(
            label="Download Resume PDF",
            data=pdf_output.getvalue(),
            file_name="resume.pdf",
            mime="application/pdf"
        )

if __name__ == "__main__":
    main()
