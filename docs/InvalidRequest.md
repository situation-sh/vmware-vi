# InvalidRequest

An InvalidRequest fault is thrown in response to a malformed request to the server that fails in the transport layer, e.g., the SOAP XML request was invalid.  Sub-types of this fault, provides more specific transport errors, such as a using a reference to an unknown managed object type or method. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from vmware_vi.models.invalid_request import InvalidRequest

# TODO update the JSON string below
json = "{}"
# create an instance of InvalidRequest from a JSON string
invalid_request_instance = InvalidRequest.from_json(json)
# print the JSON string representation of the object
print InvalidRequest.to_json()

# convert the object into a dict
invalid_request_dict = invalid_request_instance.to_dict()
# create an instance of InvalidRequest from a dict
invalid_request_form_dict = invalid_request.from_dict(invalid_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


