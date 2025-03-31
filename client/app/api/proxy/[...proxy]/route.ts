import { NextRequest, NextResponse } from "next/server";

export async function GET(
  req: NextRequest,
  { params }: { params: Promise<{ proxy: string[] }> }
) {
  return await handleProxy(req, await params);
}

export async function POST(
  req: NextRequest,
  { params }: { params: Promise<{ proxy: string[] }> }
) {
  return await handleProxy(req, await params);
}

export async function PUT(
  req: NextRequest,
  { params }: { params: Promise<{ proxy: string[] }> }
) {
  return await handleProxy(req, await params);
}

export async function PATCH(
  req: NextRequest,
  { params }: { params: Promise<{ proxy: string[] }> }
) {
  return await handleProxy(req, await params);
}

export async function DELETE(
  req: NextRequest,
  { params }: { params: Promise<{ proxy: string[] }> }
) {
  return await handleProxy(req, await params);
}

interface RequestInitWithDuplex extends RequestInit {
  duplex?: string;
}
// Common handler for all HTTP methods
async function handleProxy(req: NextRequest, params: { proxy: string[] }) {
  let backendBaseUrl = process.env.BACKEND_URL; // Default backend URL

  if (req.headers.get("x-backend-url")) {
    backendBaseUrl = req.headers.get("x-backend-url") as string;
  }

  if (!backendBaseUrl) {
    return NextResponse.json(
      { error: "Backend URL is not configured" },
      { status: 500 }
    );
  }

  if (!backendBaseUrl.endsWith("/")) {
    backendBaseUrl += "/";
  }

  // Ensure params.proxy is properly handled
  const path = params.proxy ? params.proxy.join("/") : "";
  let targetUrl = `${backendBaseUrl}${path}`;

  // Ensure the backend URL ends with a slash
  //console.log("req_url", req.url);
  if (!targetUrl.endsWith("/")) {
    targetUrl += "/";
  }

  // Append query parameters if any
  const searchParams = req.nextUrl.searchParams.toString();
  if (searchParams) {
    targetUrl += `?${searchParams}`;
  }
  if (["PATCH", "DELETE", "PUT", "POST"].includes(req.method)) {
    if (!targetUrl.endsWith("/")) {
      targetUrl += "/";
    }
  }
  console.log("targetUrl", targetUrl, "req_url", req.url);
  try {
    // Clone the headers from the incoming request
    const headers = new Headers(req.headers);

    // Detect if the request is multipart/form-data (file upload)
    const isMultipart = headers
      .get("content-type")
      ?.startsWith("multipart/form-data");

    // Set up fetch options
    const fetchOptions: RequestInitWithDuplex = {
      method: req.method,
      headers,
      body: isMultipart || req.method !== "GET" ? req.body : undefined, // Forward body directly
      duplex: "half",
    };

    const response = await fetch(targetUrl, fetchOptions);

    return new NextResponse(response.body, {
      status: response.status,
      headers: response.headers,
    });
  } catch (error) {
    console.error("Error forwarding request:", error);
    return NextResponse.json({ error: "Proxy error" }, { status: 500 });
  }
}
