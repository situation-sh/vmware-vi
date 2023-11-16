# AboutInfo

This data object type describes system information including the name, type, version, and build number. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Short form of the product name.  | 
**full_name** | **str** | The complete product name, including the version information.  | 
**vendor** | **str** | Name of the vendor of this product.  | 
**version** | **str** | Dot-separated version string.  For example, \&quot;1.2\&quot;.  | 
**patch_level** | **str** | Patch level for the server.  ***Since:*** vSphere API 7.0.2.0  | [optional] 
**build** | **str** | Build string for the server on which this call is made.  For example, x.y.z-num. This string does not apply to the API.  | 
**locale_version** | **str** | Version of the message catalog for the current session&#39;s locale.  | [optional] 
**locale_build** | **str** | Build number for the current session&#39;s locale.  Typically, this is a small number reflecting a localization change from the normal product build.  | [optional] 
**os_type** | **str** | Operating system type and architecture.  Examples of values are: - \&quot;win32-x86\&quot; - For x86-based Windows systems. - \&quot;linux-x86\&quot; - For x86-based Linux systems. - \&quot;vmnix-x86\&quot; - For the x86 ESX Server microkernel. - \&quot;vmnix-arm64\&quot; - For the arm64 ESX Server microkernel.  | 
**product_line_id** | **str** | The product ID is a unique identifier for a product line.  Examples of values are: - \&quot;gsx\&quot; - For the VMware Server product. - \&quot;esx\&quot; - For the ESX product. - \&quot;embeddedEsx\&quot; - For the ESXi product. - \&quot;esxio\&quot; - For the ESXio product. - \&quot;vpx\&quot; - For the VirtualCenter product.  | 
**api_type** | **str** | Indicates whether or not the service instance represents a standalone host.  If the service instance represents a standalone host, then the physical inventory for that service instance is fixed to that single host. VirtualCenter server provides additional features over single hosts. For example, VirtualCenter offers multi-host management.  Examples of values are: - \&quot;VirtualCenter\&quot; - For a VirtualCenter instance. - \&quot;HostAgent\&quot; - For host agent on an ESX Server or VMware Server host.  | 
**api_version** | **str** | The version of the API as a dot-separated string.  For example, \&quot;1.0.0\&quot;.  | 
**instance_uuid** | **str** | A globally unique identifier associated with this service instance.  ***Since:*** vSphere API 4.0  | [optional] 
**license_product_name** | **str** | The license product name  ***Since:*** vSphere API 4.0  | [optional] 
**license_product_version** | **str** | The license product version  ***Since:*** vSphere API 4.0  | [optional] 

## Example

```python
from vmware_vi.models.about_info import AboutInfo

# TODO update the JSON string below
json = "{}"
# create an instance of AboutInfo from a JSON string
about_info_instance = AboutInfo.from_json(json)
# print the JSON string representation of the object
print AboutInfo.to_json()

# convert the object into a dict
about_info_dict = about_info_instance.to_dict()
# create an instance of AboutInfo from a dict
about_info_form_dict = about_info.from_dict(about_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


