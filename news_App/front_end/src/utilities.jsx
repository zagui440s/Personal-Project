import axios from "axios";

export const api = axios.create({
  baseURL: "http://127.0.0.1:8000/api/v1/",
});

export const userRegistration = async (formData) => {
  const { email, password, registration } = formData;
  console.log(`Sending request to users/${registration ? "signup/" : "login/"}`); // Add this line 
  let response = await api.post(
    `users/${registration ? "signup/" : "login/"}`,
    {
      email: email,
      password: password,
    }
  );
  if (response.status === 200 || response.status === 201){
    let {token, user} = response.data
    localStorage.setItem('token', token)
    api.defaults.headers.common['Authorization'] = `Token ${token}`
    return user
  }
  alert(response.data, "utilities line 22")
  return null
};

export const signOut = async(user) => {
  let response = await api.post('users/logout/')
  if (response.status === 204){
    localStorage.removeItem("token")
    delete api.defaults.headers.common['Authorization']
    return null
  }
  alert("failure to log out")
  return user
}

export const getInfo = async() => {
  let token = localStorage.getItem('token')
  if (token){
    api.defaults.headers.common['Authorization'] = `Token ${token}`
    let response = await api.get("users/info/")
    if (response.status === 200){
      return response.data.email
    }
    return null
  }
  else{
    return null
  }
}