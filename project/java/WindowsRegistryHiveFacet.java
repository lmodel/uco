package example;

/* metamodel_version: 1.12.0 */
/* version: 1.5.0 */
import java.net.URI;
import java.time.LocalDate;
import java.time.LocalTime;
import java.time.ZonedDateTime;
import java.util.List;
import lombok.*;

/**
  A Windows registry hive facet is a grouping of characteristics unique to a particular logical group of keys, subkeys, and values in a Windows registry (a hierarchical database that stores low-level settings for the Microsoft Windows operating system and for applications that opt to use the registry). [based on https://en.wikipedia.org/wiki/Windows_Registry]
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class WindowsRegistryHiveFacet extends Facet {

  private String hiveType;


}