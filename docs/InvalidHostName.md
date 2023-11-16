# InvalidHostName

The attempted operation requires that the host has a suitable FQDN.  ***Since:*** vSphere API 4.1 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from vmware_vi.models.invalid_host_name import InvalidHostName

# TODO update the JSON string below
json = "{}"
# create an instance of InvalidHostName from a JSON string
invalid_host_name_instance = InvalidHostName.from_json(json)
# print the JSON string representation of the object
print InvalidHostName.to_json()

# convert the object into a dict
invalid_host_name_dict = invalid_host_name_instance.to_dict()
# create an instance of InvalidHostName from a dict
invalid_host_name_form_dict = invalid_host_name.from_dict(invalid_host_name_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


