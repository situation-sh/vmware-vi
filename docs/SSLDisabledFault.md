# SSLDisabledFault

A SSLDisabledFault fault occurs when a host does not have ssl enabled.  ***Since:*** vSphere API 4.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from vmware_vi.models.ssl_disabled_fault import SSLDisabledFault

# TODO update the JSON string below
json = "{}"
# create an instance of SSLDisabledFault from a JSON string
ssl_disabled_fault_instance = SSLDisabledFault.from_json(json)
# print the JSON string representation of the object
print SSLDisabledFault.to_json()

# convert the object into a dict
ssl_disabled_fault_dict = ssl_disabled_fault_instance.to_dict()
# create an instance of SSLDisabledFault from a dict
ssl_disabled_fault_form_dict = ssl_disabled_fault.from_dict(ssl_disabled_fault_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


