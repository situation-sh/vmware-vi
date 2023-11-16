# HostLicenseSpec


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**source** | [**LicenseSource**](LicenseSource.md) |  | [optional] 
**edition_key** | **str** | License edition to use  ***Since:*** vSphere API 4.0  | [optional] 
**disabled_feature_key** | **List[str]** | Disabled features.  When an edition is set, all the features in it are enabled by default. The following parameter gives a finer control on which features are disabled.  ***Since:*** vSphere API 4.0  | [optional] 
**enabled_feature_key** | **List[str]** | Enabled features  ***Since:*** vSphere API 4.0  | [optional] 

## Example

```python
from vmware_vi.models.host_license_spec import HostLicenseSpec

# TODO update the JSON string below
json = "{}"
# create an instance of HostLicenseSpec from a JSON string
host_license_spec_instance = HostLicenseSpec.from_json(json)
# print the JSON string representation of the object
print HostLicenseSpec.to_json()

# convert the object into a dict
host_license_spec_dict = host_license_spec_instance.to_dict()
# create an instance of HostLicenseSpec from a dict
host_license_spec_form_dict = host_license_spec.from_dict(host_license_spec_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


