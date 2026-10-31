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
  A computer specificaiton facet is a grouping of characteristics unique to the hardware and software of a programmable electronic device that can store, retrieve, and process data. [based on merriam-webster.com/dictionary/computer]
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class ComputerSpecificationFacet extends Facet {

  private Integer availableRam;
  private ZonedDateTime biosDate;
  private String biosManufacturer;
  private ZonedDateTime biosReleaseDate;
  private String biosSerialNumber;
  private String biosVersion;
  private String cpu;
  private String cpuFamily;
  private ZonedDateTime currentSystemDate;
  private String gpu;
  private String gpuFamily;
  private String hostname;
  private ZonedDateTime localTime;
  private List<ObservableObject> networkInterface;
  private String processorArchitecture;
  private ZonedDateTime systemTime;
  private String timezoneDST;
  private String timezoneStandard;
  private Integer totalRam;
  private String uptime;


}