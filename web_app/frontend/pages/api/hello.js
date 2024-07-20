// This is the hello.js file in the Next.js API route.

export default function handler(req, res) {
  res.status(200).json({ name: 'Hello API Route' })
}