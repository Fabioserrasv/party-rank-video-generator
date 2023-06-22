from wvalidate import Validate as v, ValidatorReturn, Validator, ValidatorError, ValidatorPath

class JsonSongsValidator(Validator):
  def __init__(self, validator) -> None:
    super().__init__()
    self.validator = validator

  def is_valid(self, data: object) -> ValidatorReturn:
    if not isinstance(data, dict):
      return ValidatorReturn(False, ValidatorError("Is not an instance of dict."))
  
    errors = []
    for index, d in data.items():
      is_valid, validator_errors = self.validator.is_valid(d)

      if not is_valid:
        for e in validator_errors:
          errors.append(
            ValidatorError(message=e.message, path=ValidatorPath(index, *e.path))
          )
    
    if len(errors) == 0:
      return ValidatorReturn(True)
    
    return ValidatorReturn(False, errors)

image_json_validator = v.dict({
  "title": v.string(),
  "participants": v.list(v.string()),
  "series": JsonSongsValidator(v.dict(
    {
      "type": v.string(),
      "anime": v.string(),
      "song": v.string(),
      "notes": v.list(v.string()),
      "average": v.numeric(),
      "cover": v.string()
    }
  ))
})