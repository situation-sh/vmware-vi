# MismatchedBundle

A MismatchedBundle fault is thrown when the bundle supplied for *HostFirmwareSystem.RestoreFirmwareConfiguration* does not match the specifications of the host  ***Since:*** VI API 2.5 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bundle_uuid** | **str** | The uuid of the host that the bundle was generated for  ***Since:*** VI API 2.5  | 
**host_uuid** | **str** | The uuid of the host  ***Since:*** VI API 2.5  | 
**bundle_build_number** | **int** | The build number of the host that the bundle was generated for  ***Since:*** VI API 2.5  | 
**host_build_number** | **int** | The build number of the host  ***Since:*** VI API 2.5  | 

## Example

```python
from vmware_vi.models.mismatched_bundle import MismatchedBundle

# TODO update the JSON string below
json = "{}"
# create an instance of MismatchedBundle from a JSON string
mismatched_bundle_instance = MismatchedBundle.from_json(json)
# print the JSON string representation of the object
print MismatchedBundle.to_json()

# convert the object into a dict
mismatched_bundle_dict = mismatched_bundle_instance.to_dict()
# create an instance of MismatchedBundle from a dict
mismatched_bundle_form_dict = mismatched_bundle.from_dict(mismatched_bundle_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


