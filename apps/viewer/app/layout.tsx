import type { Metadata } from "next"
import type React from "react"

export const metadata: Metadata = {
  title: "Deltaload Viewer",
  description: "Chronological feed of seeded bookmarks",
}

export default function RootLayout({ children }: { children: React.ReactNode }) {
  return (
    <html lang="en">
      <body style={{ margin: 0, fontFamily: "Inter, system-ui, Arial, sans-serif", background: "#0b0b0c", color: "#e6e7ea" }}>
        {children}
      </body>
    </html>
  )
}
