# DeltaDiskFormatNotSupported

Thrown on an attempt to use an unsupported delta disk format.  ***Since:*** vSphere API 5.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**datastore** | [**List[ManagedObjectReference]**](ManagedObjectReference.md) | The datastores which do not support the specified format.  ***Since:*** vSphere API 5.0  Refers instances of *Datastore*.  | [optional] 
**delta_disk_format** | **str** | The format not supported.  See *DeltaDiskFormat*.  ***Since:*** vSphere API 5.0  | 

## Example

```python
from vmware_vi.models.delta_disk_format_not_supported import DeltaDiskFormatNotSupported

# TODO update the JSON string below
json = "{}"
# create an instance of DeltaDiskFormatNotSupported from a JSON string
delta_disk_format_not_supported_instance = DeltaDiskFormatNotSupported.from_json(json)
# print the JSON string representation of the object
print DeltaDiskFormatNotSupported.to_json()

# convert the object into a dict
delta_disk_format_not_supported_dict = delta_disk_format_not_supported_instance.to_dict()
# create an instance of DeltaDiskFormatNotSupported from a dict
delta_disk_format_not_supported_form_dict = delta_disk_format_not_supported.from_dict(delta_disk_format_not_supported_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


