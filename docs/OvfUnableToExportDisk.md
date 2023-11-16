# OvfUnableToExportDisk


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**disk_name** | **str** | disk name  ***Since:*** vSphere API 4.0  | 

## Example

```python
from vmware_vi.models.ovf_unable_to_export_disk import OvfUnableToExportDisk

# TODO update the JSON string below
json = "{}"
# create an instance of OvfUnableToExportDisk from a JSON string
ovf_unable_to_export_disk_instance = OvfUnableToExportDisk.from_json(json)
# print the JSON string representation of the object
print OvfUnableToExportDisk.to_json()

# convert the object into a dict
ovf_unable_to_export_disk_dict = ovf_unable_to_export_disk_instance.to_dict()
# create an instance of OvfUnableToExportDisk from a dict
ovf_unable_to_export_disk_form_dict = ovf_unable_to_export_disk.from_dict(ovf_unable_to_export_disk_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


