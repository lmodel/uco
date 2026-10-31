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
  An image facet is a grouping of characteristics unique to a complete copy of a hard disk, memory, or other digital media.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class ImageFacet extends Facet {

  private String imageType;


}