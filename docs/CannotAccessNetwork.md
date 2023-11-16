# CannotAccessNetwork

A network associated with the virtual machine is not accessible.  If returned as part of migration checks, this is an error if either of the following is true, a warning otherwise: - The virtual ethernet card device backing is a distributed virtual switch,   of which the destination host is not a member - The virtual ethernet card device backing is a standard network and the   the device is connected 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**network** | [**ManagedObjectReference**](ManagedObjectReference.md) |  | [optional] 

## Example

```python
from vmware_vi.models.cannot_access_network import CannotAccessNetwork

# TODO update the JSON string below
json = "{}"
# create an instance of CannotAccessNetwork from a JSON string
cannot_access_network_instance = CannotAccessNetwork.from_json(json)
# print the JSON string representation of the object
print CannotAccessNetwork.to_json()

# convert the object into a dict
cannot_access_network_dict = cannot_access_network_instance.to_dict()
# create an instance of CannotAccessNetwork from a dict
cannot_access_network_form_dict = cannot_access_network.from_dict(cannot_access_network_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


