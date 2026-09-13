import argparse
import sys
from typing import Optional

from rag_pipeline import create_vector_store


def main() -> None:
    parser = argparse.ArgumentParser(description="Simple runner for the RAG pipeline")
    parser.add_argument("--data", default="data", help="Path to data folder containing PDFs")
    parser.add_argument("--save", default=None, help="Directory to save the FAISS index (optional)")
    args = parser.parse_args()

    try:
        vs = create_vector_store(args.data)
        print("Vectorstore created:", type(vs).__name__)

        if args.save:
            if hasattr(vs, "save_local"):
                vs.save_local(args.save)
                print(f"Saved vectorstore to {args.save}")
            elif hasattr(vs, "persist"):
                vs.persist(args.save)
                print(f"Persisted vectorstore to {args.save}")
            else:
                print("No supported save method found on vectorstore; skipping save.")

        # Try to show a basic stat about stored vectors/docs
        n: Optional[int] = None
        try:
            if hasattr(vs, "index") and hasattr(vs.index, "ntotal"):
                n = vs.index.ntotal
            elif hasattr(vs, "docstore"):
                try:
                    n = len(vs.docstore._dict)  # best-effort
                except Exception:
                    n = None
        except Exception:
            n = None

        if n is not None:
            print(f"Stored vectors: {n}")

    except Exception as e:
        print("Error creating vectorstore:", e)
        sys.exit(1)


if __name__ == "__main__":
    main()
