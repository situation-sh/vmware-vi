# ExtensionOvfConsumerInfo

This data object contains configuration for extensions that also extend the OVF functionality of vCenter server.  **Note:** This feature is for internal use only.  ***Since:*** vSphere API 5.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**callback_url** | **str** | Callback url for the OVF consumer.  This URL must point to a SOAP API implementing the OVF consumer interface.  Example: https://extension-host:8081/  This callback is for internal use only.  ***Since:*** vSphere API 5.0  | 
**section_type** | **List[str]** | A list of fully qualified OVF section types that this consumer handles.  Fully qualified means that each section type must be prefixed with its namespace enclosed in curly braces. See the examples below.  An InvalidArgument error is thrown if there is overlap between OVF consumers, meaning that the same section type appears in the sectionType list of more than one OVF consumer.  Example: \\[ \&quot;{http://www.vmware.com/schema/vServiceManager}vServiceDependency\&quot;, \&quot;{http://www.vmware.com/schema/vServiceManager}vServiceBinding\&quot; \\]  ***Since:*** vSphere API 5.0  | 

## Example

```python
from vmware_vi.models.extension_ovf_consumer_info import ExtensionOvfConsumerInfo

# TODO update the JSON string below
json = "{}"
# create an instance of ExtensionOvfConsumerInfo from a JSON string
extension_ovf_consumer_info_instance = ExtensionOvfConsumerInfo.from_json(json)
# print the JSON string representation of the object
print ExtensionOvfConsumerInfo.to_json()

# convert the object into a dict
extension_ovf_consumer_info_dict = extension_ovf_consumer_info_instance.to_dict()
# create an instance of ExtensionOvfConsumerInfo from a dict
extension_ovf_consumer_info_form_dict = extension_ovf_consumer_info.from_dict(extension_ovf_consumer_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


