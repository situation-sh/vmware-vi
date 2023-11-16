# LimitExceeded

This exception is thrown if one of the arguments passed to the function exceeds a limit.  ***Since:*** vSphere API 4.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_property** | **str** | The name of the property that exceeds the limit.  ***Since:*** vSphere API 4.0  | [optional] 
**limit** | **int** | The limit value.  ***Since:*** vSphere API 4.0  | [optional] 

## Example

```python
from vmware_vi.models.limit_exceeded import LimitExceeded

# TODO update the JSON string below
json = "{}"
# create an instance of LimitExceeded from a JSON string
limit_exceeded_instance = LimitExceeded.from_json(json)
# print the JSON string representation of the object
print LimitExceeded.to_json()

# convert the object into a dict
limit_exceeded_dict = limit_exceeded_instance.to_dict()
# create an instance of LimitExceeded from a dict
limit_exceeded_form_dict = limit_exceeded.from_dict(limit_exceeded_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


