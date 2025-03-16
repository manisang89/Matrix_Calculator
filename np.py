import numpy as np
import streamlit as st
st.markdown(
    """
    <style>
    html, body, [class*="st-"] {
        font-size: 20px !important;
    }
    .stMarkdown h1 {
        font-size: 32px !important;
    }
    .stMarkdown h2 {
        font-size: 28px !important;
        }
    .stMarkdown h3 {
        font-size: 24px !important;
    }
    div.stButton > button {
        background-color: #4CAF50 !important; /* Green */
        color: white !important;
        border-radius: 8px;
        padding: 10px 20px;
        font-size: 16px;
        border: none;
    }
    div[data-baseweb="input"] input {
        font-size: 18px !important;
    }
    div[data-baseweb="select"] span {
        font-size: 18px !important;
    }
    .stTitle {
        font-size: 36px !important;
    </style>
    """,
    unsafe_allow_html=True
)
st.title("Basic Matrix operations")
op=st.selectbox("Selected from list of options to perform operations",options=["Addition","Subtraction","Multiplication","Transpose","Scalar Multiplication","Determinant","Inverse"])
matrix1, matrix2 = None, None
if op in ["Addition","Subtraction"]:
    
    row1=st.number_input("Enter the row1 size ",min_value=1,step=1)
    col1=st.number_input("Enter the column1 size ",min_value=1,step=1)
    inp1=st.text_input("Enter the values separated by commas as row traveral",key="inp1")

    row2=st.number_input("Enter the row2 size ",min_value=1,step=1)
    col2=st.number_input("Enter the column2 size ",min_value=1,step=1)
    inp2=st.text_input("Enter the values separated by commas as row traveral",key="inp2")
    if inp1 and inp2:
        try:
            li1=list(map(float,inp1.split(",")))
            li2=list(map(float,inp2.split(",")))

            if len(li1)!=row1*col1 or len(li2)!=row2*col2 or row1!=row2 or col1!=col2:
                raise ValueError(f"Mismatch of size or wrong input")
    
            matrix1=np.array(li1).reshape(row1,col1)
            matrix2=np.array(li2).reshape(row2,col2)
            

            st.write("Matrix 1:")
            st.write(matrix1)
            st.write("Matrix 2:")
            st.write(matrix2)

            if st.button("Calculate",):
                if op=="Addition":
                    r=matrix1+matrix2
                    st.write("Addition of matrix : ")
                elif op=="Subtraction":
                    r=matrix1-matrix2
                    st.write("Subtraction of matrix : ")
                st.write(r)

        except ValueError as e:
            st.error(f"Error: ",{e})

elif op == "Multiplication":
    row1=st.number_input("Enter the row1 size ",min_value=1,step=1)
    col1=st.number_input("Enter the column1 size ",min_value=1,step=1)
    inp1=st.text_input("Enter the values separated by commas as row traveral",key="inp1")

    row2=st.number_input("Enter the row2 which is equal to column1 size ",min_value=1,step=1)
    col2=st.number_input("Enter the column2 size ",min_value=1,step=1)
    inp2=st.text_input("Enter the values separated by commas as row traveral",key="inp2")
    if inp1 and inp2:
        try:
            li1=list(map(float,inp1.split(",")))
            li2=list(map(float,inp2.split(",")))

            if len(li1)!=row1*col1 or len(li2)!=row2*col2 or col1!=row2:
                raise ValueError(f"Mismatch of size or wrong input")
            
            matrix1=np.array(li1).reshape(row1,col1)
            matrix2=np.array(li2).reshape(row2,col2)

            st.write("Matrix 1:")
            st.write(matrix1)
            st.write("Matrix 2:")
            st.write(matrix2)
            if st.button("Calculate"):
                r=np.dot(matrix1,matrix2)
                st.write("Multiplication of matrix : ")
                st.write(r)
                
        except ValueError as e:
            st.error(f"Error",{e})
    
elif op=="Scalar Multiplication":
    row=st.number_input("Enter the row size ",min_value=1,step=1)
    col=st.number_input("Enter the column size ",min_value=1,step=1)
    inp=st.text_input("Enter the values separated by commas as row traveral",key="inp")
    n=st.number_input("Enter scalar to multiply ",min_value=1,step=1)
    if inp:
        try:
            li=list(map(float,inp.split(",")))
            matrix=np.array(li).reshape(row,col)
            if len(li)!=row*col:
                raise ValueError(f"Mismatch of size or wrong input")
            st.write("Matrix : ")
            st.write(matrix)
            if st.button("Calculate"):
                r=n*matrix
                st.write("Scalar Multiplication of matrix : ")
                st.write(r)
        except ValueError as e:
            st.error(f"Error",{e})

elif op=="Determinant":
    row=st.number_input("Enter the size ",min_value=1,step=1)
    inp=st.text_input("Enter the values separated by commas as row traveral ",(row*row),key="inp")
    if inp:
        try:
            li=list(map(float,inp.split(",")))
            matrix=np.array(li).reshape(row,row)
            if len(li)!=row*row:
                raise ValueError(f"Mismatch of size or wrong input")
            st.write("Matrix : ")
            st.write(matrix)
            if st.button("Calculate"):
                r=np.linalg.det(matrix)
                st.write("Determinant of matrix : ")
                st.write(r)
        except ValueError as e:
            st.error(f"Error",{e})

elif op=="Inverse":
    row=st.number_input("Enter the size ",min_value=1,step=1)
    inp=st.text_input("Enter the values separated by commas as row traveral",(row*row),key="inp")
    if inp:
        try:
            li=list(map(float,inp.split(",")))
            matrix=np.array(li).reshape(row,row)
            if len(li)!=row*row :
                raise ValueError(f"Mismatch of size or wrong input")
            st.write("Matrix : ")
            st.write(matrix)
            if st.button("Calculate"):
                if np.linalg.det(matrix)==0:
                    st.error("Inverse of matrix does not exist")
                r=np.linalg.inv(matrix)
                st.write("Inverse of matrix : ")
                st.write(r)
        except ValueError as e:
            st.error(f"Error",{e})

elif op=="Transpose":
    row=st.number_input("Enter the row size ",min_value=1,step=1)
    col=st.number_input("Enter the column size ",min_value=1,step=1)
    inp=st.text_input("Enter the values separated by commas as row traveral",key="inp")
    if inp:
        try:
            li=list(map(float,inp.split(",")))
            matrix=np.array(li).reshape(row,col)
            if len(li)!=row*col :
                raise ValueError(f"Mismatch of size or wrong input")
            st.write("Matrix : ")
            st.write(matrix)
            if st.button("Calculate"):
                r=np.transpose(matrix)
                st.write("Transpose of matrix : ")
                st.write(r)
        except ValueError as e:
            st.error(f"Error",{e})

