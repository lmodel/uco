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
  A raster picture facet is a grouping of characteristics unique to a raster (or bitmap) image.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class RasterPictureFacet extends Facet {

  private Integer bitsPerPixel;
  private ObservableObject camera;
  private String imageCompressionMethod;
  private Integer pictureHeight;
  private String pictureType;
  private Integer pictureWidth;


}