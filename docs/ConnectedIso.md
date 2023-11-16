# ConnectedIso


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cdrom** | [**VirtualCdrom**](VirtualCdrom.md) |  | 
**filename** | **str** | The filename of the ISO  ***Since:*** vSphere API 4.0  | 

## Example

```python
from vmware_vi.models.connected_iso import ConnectedIso

# TODO update the JSON string below
json = "{}"
# create an instance of ConnectedIso from a JSON string
connected_iso_instance = ConnectedIso.from_json(json)
# print the JSON string representation of the object
print ConnectedIso.to_json()

# convert the object into a dict
connected_iso_dict = connected_iso_instance.to_dict()
# create an instance of ConnectedIso from a dict
connected_iso_form_dict = connected_iso.from_dict(connected_iso_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


