import streamlit as st
import re

def password_strength(password):
    strength = 0
    remarks = ""

    if len(password) >= 8:
        strength += 1
    if re.search(r"[a-z]", password) and re.search(r"[A-Z]", password):
        strength += 1
    if re.search(r"\d", password):
        strength += 1
    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        strength += 1

    if strength == 0:
        remarks = "Very Weak"
    elif strength == 1:
        remarks = "Weak"
    elif strength == 2:
        remarks = "Moderate"
    elif strength == 3:
        remarks = "Strong"
    elif strength == 4:
        remarks = "Very Strong"

    return strength, remarks

# Streamlit App
st.title("🔒 Password Strength Meter")

password = st.text_input("Enter your password", type="password")

if password:
    strength, remarks = password_strength(password)

    st.write(f"**Strength Score:** {strength} / 4")
    st.success(f"**Password is:** {remarks}")

    if strength < 3:
        st.warning("⚠️ Try to make your password stronger by adding uppercase, lowercase, numbers, and special characters.")
    else:
        st.balloons()
