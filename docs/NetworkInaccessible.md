# NetworkInaccessible

This fault is thrown when an operation to configure a NAS volume fails because network access is unavailable.  ***Since:*** vSphere API 4.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from vmware_vi.models.network_inaccessible import NetworkInaccessible

# TODO update the JSON string below
json = "{}"
# create an instance of NetworkInaccessible from a JSON string
network_inaccessible_instance = NetworkInaccessible.from_json(json)
# print the JSON string representation of the object
print NetworkInaccessible.to_json()

# convert the object into a dict
network_inaccessible_dict = network_inaccessible_instance.to_dict()
# create an instance of NetworkInaccessible from a dict
network_inaccessible_form_dict = network_inaccessible.from_dict(network_inaccessible_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


