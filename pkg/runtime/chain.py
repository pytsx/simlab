from typing import Callable, Any

def Chain[T](
    *args: Callable[[Any], Any],
    final: Callable[[Any], T],
) -> T:
    data: Any = None

    for step in args:
        try:
            data = step(data)
        except Exception as e:
            raise RuntimeError(
                f"Chain step failed: {e}"
            ) from e

    try:
        return final(data)
    except Exception as e:
        raise RuntimeError(
            f"Pipeline callback failed: {e}"
        ) from e