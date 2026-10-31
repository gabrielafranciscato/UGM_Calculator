from datetime import datetime
from typing import List, Dict, Any, Optional

# Represents a single calculation record with its expression, result, and timestamp.
class CalculationRecord:
    def __init__(self, expression: str, result: Any):
        self.expression: str = expression
        self.result: Any = result
        self.timestamp: datetime = datetime.now()

    def to_dict(self) -> Dict[str, Any]:
        """Converts the record into a dictionary format."""
        return {
            "expression": self.expression,
            "result": self.result,
            "timestamp": self.timestamp.isoformat()
        }

# Manages the history of calculations, ensuring valid entries and providing retrieval methods.
class CalculationHistoryManager:
    def __init__(self):
        self._history: List[CalculationRecord] = []

    def record_calculation(self, expression: str, result: Any) -> bool:
        if not self._is_valid_calculation(expression, result):
            return False

        record = CalculationRecord(expression, result)
        self._history.append(record)
        return True

    def retrieve_history(self) -> List[Dict[str, Any]]:
        return [record.to_dict() for record in self._history]

    def clear_history(self) -> None:
        self._history.clear()

    def get_latest_calculation(self) -> Optional[Dict[str, Any]]:
        if not self._history:
            return None
        return self._history[-1].to_dict()

#Ensures that the calculation is valid before recording it in the history.
    def _is_valid_calculation(self, expression: str, result: Any) -> bool:
        if not expression or not expression.strip():
            return False

        if result is None:
            return False

        if isinstance(result, str) and ("error" in result.lower() or "nan" in result.lower()):
            return False

        return True