# CannotUseNetwork

A network associated with the virtual machine is accessible, but it cannot be used for some reason.  ***Since:*** vSphere API 5.5 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**device** | **str** | The label of the network device.  ***Since:*** vSphere API 5.5  | 
**backing** | **str** | The backing of the network device.  ***Since:*** vSphere API 5.5  | 
**connected** | **bool** | The connected/disconnected state of the device.  ***Since:*** vSphere API 5.5  | 
**reason** | **str** | Reason describing why the network cannot be used.  ***Since:*** vSphere API 5.5  | 
**network** | [**ManagedObjectReference**](ManagedObjectReference.md) |  | [optional] 

## Example

```python
from vmware_vi.models.cannot_use_network import CannotUseNetwork

# TODO update the JSON string below
json = "{}"
# create an instance of CannotUseNetwork from a JSON string
cannot_use_network_instance = CannotUseNetwork.from_json(json)
# print the JSON string representation of the object
print CannotUseNetwork.to_json()

# convert the object into a dict
cannot_use_network_dict = cannot_use_network_instance.to_dict()
# create an instance of CannotUseNetwork from a dict
cannot_use_network_form_dict = cannot_use_network.from_dict(cannot_use_network_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


