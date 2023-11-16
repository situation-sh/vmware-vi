# AlreadyConnected

AlreadyConnect fault is thrown by the host connect method if the host is already connected to a VirtualCenter server.  This might occur if the host has been added more than once in the same VirtualCenter in different folders or compute resources. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Name of the host  | 

## Example

```python
from vmware_vi.models.already_connected import AlreadyConnected

# TODO update the JSON string below
json = "{}"
# create an instance of AlreadyConnected from a JSON string
already_connected_instance = AlreadyConnected.from_json(json)
# print the JSON string representation of the object
print AlreadyConnected.to_json()

# convert the object into a dict
already_connected_dict = already_connected_instance.to_dict()
# create an instance of AlreadyConnected from a dict
already_connected_form_dict = already_connected.from_dict(already_connected_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


