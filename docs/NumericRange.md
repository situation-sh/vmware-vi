# NumericRange

The class that describe an integer range.  ***Since:*** vSphere API 4.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**start** | **int** | The starting number.  ***Since:*** vSphere API 4.0  | 
**end** | **int** | The ending number (inclusive).  ***Since:*** vSphere API 4.0  | 

## Example

```python
from vmware_vi.models.numeric_range import NumericRange

# TODO update the JSON string below
json = "{}"
# create an instance of NumericRange from a JSON string
numeric_range_instance = NumericRange.from_json(json)
# print the JSON string representation of the object
print NumericRange.to_json()

# convert the object into a dict
numeric_range_dict = numeric_range_instance.to_dict()
# create an instance of NumericRange from a dict
numeric_range_form_dict = numeric_range.from_dict(numeric_range_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


