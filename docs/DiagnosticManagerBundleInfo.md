# DiagnosticManagerBundleInfo

Describes a location of a diagnostic bundle and the server to which it belongs.  This is a return type for the generateLogBundles operation. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**system** | [**ManagedObjectReference**](ManagedObjectReference.md) |  | [optional] 
**url** | **str** | The location from which the diagnostic bundle can be downloaded.  The host part of the URL is returned as &#39;\\*&#39; if the hostname to be used is the name of the server to which the call was made. For example, if the call is made to vcsrv1.domain1.com, and the bundle is available for download from http://vcsrv1.domain1.com/diagnostics/bundle.zip, the URL returned may be http:// \\* /diagnostics/bundle.zip. The client replaces the asterisk with the server name on which it invoked the call.  | 

## Example

```python
from vmware_vi.models.diagnostic_manager_bundle_info import DiagnosticManagerBundleInfo

# TODO update the JSON string below
json = "{}"
# create an instance of DiagnosticManagerBundleInfo from a JSON string
diagnostic_manager_bundle_info_instance = DiagnosticManagerBundleInfo.from_json(json)
# print the JSON string representation of the object
print DiagnosticManagerBundleInfo.to_json()

# convert the object into a dict
diagnostic_manager_bundle_info_dict = diagnostic_manager_bundle_info_instance.to_dict()
# create an instance of DiagnosticManagerBundleInfo from a dict
diagnostic_manager_bundle_info_form_dict = diagnostic_manager_bundle_info.from_dict(diagnostic_manager_bundle_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


