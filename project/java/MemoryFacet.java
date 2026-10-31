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
  A memory facet is a grouping of characteristics unique to a particular region of temporary information storage (e.g., RAM (random access memory), ROM (read only memory)) on a digital device.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class MemoryFacet extends Facet {

  private String blockType;
  private Boolean isInjected;
  private Boolean isMapped;
  private Boolean isProtected;
  private Boolean isVolatile;
  private List<String> regionEndAddress;
  private Integer regionSize;
  private List<String> regionStartAddress;


}