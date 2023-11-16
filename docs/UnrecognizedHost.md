# UnrecognizedHost

A UnrecognizedHost is thrown if the VirtualCenter server fails to validate the identity of the host using host-key.  If a reconnect is attempted on a host and if the host-key of the host has changed since the last successful connection attempt, (might be changed by another instance of VirtualCenter), VirtualCenter server will fail to recognize the host.  ***Since:*** VI API 2.5 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**host_name** | **str** | Host in the VirtualCenter inventory which failed the identity validation.  ***Since:*** VI API 2.5  | 

## Example

```python
from vmware_vi.models.unrecognized_host import UnrecognizedHost

# TODO update the JSON string below
json = "{}"
# create an instance of UnrecognizedHost from a JSON string
unrecognized_host_instance = UnrecognizedHost.from_json(json)
# print the JSON string representation of the object
print UnrecognizedHost.to_json()

# convert the object into a dict
unrecognized_host_dict = unrecognized_host_instance.to_dict()
# create an instance of UnrecognizedHost from a dict
unrecognized_host_form_dict = unrecognized_host.from_dict(unrecognized_host_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


