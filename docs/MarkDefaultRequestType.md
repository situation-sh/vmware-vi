# MarkDefaultRequestType

The parameters of *CryptoManagerKmip.MarkDefault*. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cluster_id** | [**KeyProviderId**](KeyProviderId.md) |  | 

## Example

```python
from vmware_vi.models.mark_default_request_type import MarkDefaultRequestType

# TODO update the JSON string below
json = "{}"
# create an instance of MarkDefaultRequestType from a JSON string
mark_default_request_type_instance = MarkDefaultRequestType.from_json(json)
# print the JSON string representation of the object
print MarkDefaultRequestType.to_json()

# convert the object into a dict
mark_default_request_type_dict = mark_default_request_type_instance.to_dict()
# create an instance of MarkDefaultRequestType from a dict
mark_default_request_type_form_dict = mark_default_request_type.from_dict(mark_default_request_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


