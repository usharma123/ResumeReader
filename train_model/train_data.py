import pandas as pd

# Expanded sample data
data = {
    'filename': [
        'resume1.pdf', 'resume2.docx', 'resume3.pdf', 'resume4.docx', 'resume5.pdf',
        'resume6.pdf', 'resume7.docx', 'resume8.pdf', 'resume9.docx', 'resume10.pdf',
        'resume11.pdf', 'resume12.docx', 'resume13.pdf', 'resume14.docx', 'resume15.pdf',
        'resume16.pdf', 'resume17.docx', 'resume18.pdf', 'resume19.docx', 'resume20.pdf'
    ],
    'text': [
        'Experienced software engineer with expertise in Python, Java, and C++. Proven track record in machine learning and data analysis.',
        'Biomedical engineer with experience in signal processing, neural networks, and genomics. Skilled in biotechnology and bioinformatics.',
        'Research scientist with a focus on clinical trials, data collection, and literature review. Strong background in experimental design and analysis.',
        'Data scientist proficient in Python, machine learning, and deep learning. Experienced in using TensorFlow and PyTorch for natural language processing.',
        'Software developer with experience in Java, C++, and Python. Worked on various projects involving machine learning and data analysis.',
        'Project manager with experience in agile methodologies, project planning, and team leadership. Skilled in risk management and stakeholder communication.',
        'Marketing specialist with expertise in digital marketing, content creation, and SEO. Proven ability in social media management and campaign optimization.',
        'Financial analyst with strong skills in financial modeling, data analysis, and budgeting. Experienced in using Excel and financial software tools.',
        'Mechanical engineer with experience in CAD design, thermodynamics, and materials science. Skilled in product development and testing.',
        'Electrical engineer proficient in circuit design, embedded systems, and signal processing. Experienced in using MATLAB and Simulink.',
        'Civil engineer with expertise in structural analysis, construction management, and geotechnical engineering. Skilled in using AutoCAD and Civil 3D.',
        'Chemical engineer with experience in process engineering, chemical reactions, and safety protocols. Skilled in laboratory techniques and equipment maintenance.',
        'Architect with strong skills in architectural design, project management, and sustainability. Experienced in using Revit and SketchUp.',
        'HR manager with expertise in recruitment, employee relations, and performance management. Skilled in HR policies and compliance.',
        'Business analyst proficient in data analysis, business process improvement, and requirements gathering. Experienced in using SQL and business intelligence tools.',
        'Graphic designer with skills in Adobe Creative Suite, branding, and UX/UI design. Proven ability in creating visual content and marketing materials.',
        'Healthcare professional with experience in patient care, medical documentation, and healthcare administration. Skilled in EMR systems and patient communication.',
        'Environmental scientist with expertise in environmental assessments, sustainability, and regulatory compliance. Skilled in data analysis and fieldwork.',
        'Teacher with experience in curriculum development, classroom management, and student assessment. Skilled in educational technology and instructional design.',
        'Lawyer with expertise in legal research, contract law, and litigation. Skilled in case management and legal writing.'
    ],
    'skills': [
        'python,java,c++,machine learning,data analysis',
        'biomedical,signal processing,neural networks,genomics,biotechnology,bioinformatics',
        'research,clinical trials,data collection,literature review,experimental design,analysis',
        'python,machine learning,deep learning,tensorflow,pytorch,natural language processing',
        'java,c++,python,machine learning,data analysis',
        'agile methodologies,project planning,team leadership,risk management,stakeholder communication',
        'digital marketing,content creation,SEO,social media management,campaign optimization',
        'financial modeling,data analysis,budgeting,excel,financial software tools',
        'CAD design,thermodynamics,materials science,product development,testing',
        'circuit design,embedded systems,signal processing,MATLAB,Simulink',
        'structural analysis,construction management,geotechnical engineering,AutoCAD,Civil 3D',
        'process engineering,chemical reactions,safety protocols,laboratory techniques,equipment maintenance',
        'architectural design,project management,sustainability,Revit,SketchUp',
        'recruitment,employee relations,performance management,HR policies,compliance',
        'data analysis,business process improvement,requirements gathering,SQL,business intelligence tools',
        'Adobe Creative Suite,branding,UX/UI design,visual content,marketing materials',
        'patient care,medical documentation,healthcare administration,EMR systems,patient communication',
        'environmental assessments,sustainability,regulatory compliance,data analysis,fieldwork',
        'curriculum development,classroom management,student assessment,educational technology,instructional design',
        'legal research,contract law,litigation,case management,legal writing'
    ]
}

# Create DataFrame
df = pd.DataFrame(data)

# Save to CSV
annotated_sample_file_path = '/Users/utsavsharma/Desktop/RR/train_model/annotated_sample_resumes_20.csv'
df.to_csv(annotated_sample_file_path, index=False)

# Display the DataFrame
df.head()
