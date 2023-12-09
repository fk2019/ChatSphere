document.addEventListener('DOMContentLoaded', fetchData);

const users_url = 'http://127.0.0.1:3000/api/v1/users'
try {
  const resp = await fetch(users_url);
  if(!resp.ok) throw new Error(`Network response not okay, status: ${resp.status}`)
  const data = await rep.json()
  console.log(data)
} catch (err) {
  console.error('Fetch error', err.message);
}
