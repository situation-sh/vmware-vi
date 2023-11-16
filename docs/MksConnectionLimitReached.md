# MksConnectionLimitReached

Thrown when a mouse-keyboard-screen connection ticket to a virtual machine cannot be granted because the configured connection limit has been reached.  ***Since:*** vSphere API 5.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**connection_limit** | **int** | MKS connection limit for the virtual machine.  ***Since:*** vSphere API 5.0  | 

## Example

```python
from vmware_vi.models.mks_connection_limit_reached import MksConnectionLimitReached

# TODO update the JSON string below
json = "{}"
# create an instance of MksConnectionLimitReached from a JSON string
mks_connection_limit_reached_instance = MksConnectionLimitReached.from_json(json)
# print the JSON string representation of the object
print MksConnectionLimitReached.to_json()

# convert the object into a dict
mks_connection_limit_reached_dict = mks_connection_limit_reached_instance.to_dict()
# create an instance of MksConnectionLimitReached from a dict
mks_connection_limit_reached_form_dict = mks_connection_limit_reached.from_dict(mks_connection_limit_reached_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


