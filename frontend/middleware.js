import { NextResponse } from "next/server";

export function middleware(request) {
  const token = request.cookies.get("access_token");

  if (request.nextUrl.pathname === "/login") {
    return NextResponse.next();
  }

  if (!token) {
    return NextResponse.redirect(new URL("/login", request.url));
  }

  return NextResponse.next();
}

export const config = {
  matcher: ["/((?!api|_next/static|_next/image|favicon.ico).*)"],
};
