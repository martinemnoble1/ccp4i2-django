import { defineConfig } from "vite";
import { fileURLToPath } from "url";
import path from "path";
const __dirname = path.dirname(__filename);

export default defineConfig({
  build: {
    outDir: "dist",
    target: "node18", // target Node, not browser
    ssr: true, // <== CRUCIAL: treat this as a server-side build
    rollupOptions: {
      input: path.resolve(__dirname, "main/index.ts"),
      output: {
        entryFileNames: "main.js",
        format: "esm",
      },
      external: [
        "electron",
        "fs",
        "path",
        "os",
        "stubborn-fs",
        "node:process",
        "node:util",
        "node:os",
        "node:net",
        "node:url",
        "next",
        "electron-store",
        "detect-port",
        "child_process",
      ], // add more if needed
    },
  },
});
