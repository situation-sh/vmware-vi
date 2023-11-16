# NoHost

A NoHostFault fault occurs when a host cannot be reached. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 

## Example

```python
from vmware_vi.models.no_host import NoHost

# TODO update the JSON string below
json = "{}"
# create an instance of NoHost from a JSON string
no_host_instance = NoHost.from_json(json)
# print the JSON string representation of the object
print NoHost.to_json()

# convert the object into a dict
no_host_dict = no_host_instance.to_dict()
# create an instance of NoHost from a dict
no_host_form_dict = no_host.from_dict(no_host_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


